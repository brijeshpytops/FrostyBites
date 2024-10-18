from django.db import models
from FBApps.master.models import TimeStamp
from FBApps.master.helpers.UNIQUE.createPrimaryKey import generatePrimaryKey
# Create your models here.

class Categories(TimeStamp):
    POSTFIX = 'cake_category'
    category_id = models.CharField(primary_key=True, blank=True, null=False, max_length=255)
    name = models.CharField(max_length=255, null=False, unique=True, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.category_id = generatePrimaryKey(self.POSTFIX)
        super(Categories, self).save(*args, **kwargs)

class Cakes(TimeStamp):
    POSTFIX = 'cake'
    cake_id = models.CharField(primary_key=True, blank=True, null=False, max_length=255)
    image = models.ImageField(upload_to='cake_images/', null=False, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.cake_id = generatePrimaryKey(self.POSTFIX)
        super(Cakes, self).save(*args, **kwargs)
