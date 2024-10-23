from django.contrib import admin
from django.utils.html import format_html
from .models import Categories, Cakes, CustomizeCake, Cart
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Categories, CategoriesAdmin)


class CakesAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_image', 'description', 'price']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;"/>', obj.image.url)
        return "No Image"
    
    display_image.short_description = 'Image'
admin.site.register(Cakes, CakesAdmin)

class CustomizeCakeAdmin(admin.ModelAdmin):
    list_display = ['customer', 'display_image', 'content','request_status']
    list_filter = ['request_status']

    list_per_page = 10

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;"/>', obj.image.url)
        return "No Image"
    
    display_image.short_description = 'Image'


admin.site.register(CustomizeCake, CustomizeCakeAdmin)

admin.site.register(Cart)