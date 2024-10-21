from django.contrib import admin
from .models import Customers, CustomerProfile
# Register your models here.

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'email', 'mobile', 'is_active']
    list_filter = ['is_active']
    search_fields = ['customer_id', 'email', 'mobile']
    list_editable = ['mobile']
    list_per_page = 50
admin.site.register(Customers, CustomersAdmin)
admin.site.register(CustomerProfile)