from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.

admin.site.site_header = "FrostyBites Admin"
admin.site.index_title = "MY DASHBOARD"
admin.site.site_title = "FROSTYBITS"


admin.site.unregister(User)
admin.site.unregister(Group)