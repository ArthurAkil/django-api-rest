from django.contrib import admin

from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "birth_date",)
    search_fields = ("name", "email", "birth_date",)
    list_filter = ("name", "email", "birth_date",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")
    search_fields = ("name", "price", "stock")
    list_filter = ("name", "price", "stock")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("client","date_order",)
