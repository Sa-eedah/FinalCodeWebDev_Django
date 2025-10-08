from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'rating')
    prepopulated_fields = {'slug': ('name',)}
