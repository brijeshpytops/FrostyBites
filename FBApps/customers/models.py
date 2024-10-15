from django.db import models
from django.contrib.auth.hashers import make_password

from FBApps.master.models import TimeStamp
from FBApps.master.helpers.UNIQUE.createPrimaryKey import generatePrimaryKey

# Create your models here.
class Customers(TimeStamp):
    POSTFIX = 'customer'
    customer_id = models.CharField(primary_key=True, blank=True, null=False, max_length=255)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    mobile = models.CharField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=True, null=False, default="1234")
    is_active = models.BooleanField(default=False) 
    otp = models.CharField(max_length=255, default="546345")

    def save(self, *args, **kwargs):
        if not self.customer_id:
            self.customer_id = generatePrimaryKey(self.POSTFIX)
            self.password = make_password(self.password)
        super(Customers, self).save(*args, **kwargs)

       
        profile, created = CustomerProfile.objects.get_or_create(
            customer=self,  # Look up by the customer foreign key
            defaults={
                'profile_picture': 'default_images/customer_profile.jpg'  # Set default profile picture if creating a new profile
            }
        )
        if created:
            print(f"Profile created for customer {self.email}")
        else:
            print(f"Profile already exists for customer {self.email}")


class CustomerProfile(TimeStamp):
    POSTFIX = 'customer_profile'
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='customer_profile_pictures', blank=True, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
