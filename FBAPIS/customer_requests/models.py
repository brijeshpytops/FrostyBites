from django.db import models
from FBApps.master.models import TimeStamp
from FBApps.master.helpers.UNIQUE.createPrimaryKey import generatePrimaryKey
# Create your models here.


class CustomerRequests(TimeStamp):
    request_id = models.CharField(primary_key=True, max_length=255, blank=True, null=False)
    customer_id = models.CharField(max_length=255, null=False, blank=False)
    messages = models.TextField()

    def save(self, *args, **kwargs):
        if not self.request_id:
            self.request_id = generatePrimaryKey('customer_request')
        super(CustomerRequests, self).save(*args, **kwargs)