from django.contrib import admin
from .models import Customers, CustomerProfile
# Register your models here.

admin.site.register(Customers)
admin.site.register(CustomerProfile)