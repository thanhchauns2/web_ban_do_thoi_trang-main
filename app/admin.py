from os import access
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import(
    Customer,
    Product,
    Cart, 
    OrderPlaced
)

# Register your models here.
# username: admin
# gmail: admin@gmail.com
# pass: @Admin1

# accBusiness
# tandattranld@gmail.com 
# @Admin123
# US

# accPersonal
# tandatld2099@gmail.com 
# @Admin234
# US

# username: TL209
# gmail: tandatld2099@gmail.com
# pass: @Admin234

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info','quantity', 'ordered_date', 'status']

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
