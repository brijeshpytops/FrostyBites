from django.contrib import admin
from django.utils.html import format_html
from .models import Categories, Cakes, CustomizeCake, Cart, Order, OrderItem
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

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'order_date', 'total_amount', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('order_id', 'customer__name', 'status')
    date_hierarchy = 'order_date'
    inlines = [OrderItemInline]
    list_per_page = 20  # Pagination: 20 orders per page

    # Optional: If you want to customize the ordering
    ordering = ('-order_date',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'cake', 'quantity', 'price')
    list_filter = ('order__status',)
    search_fields = ('order__order_id', 'cake__name')
    list_per_page = 20  # Pagination: 20 items per page

    # Optional: Custom ordering
    ordering = ('order',)



