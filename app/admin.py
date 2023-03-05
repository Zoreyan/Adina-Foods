from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProdcutAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')