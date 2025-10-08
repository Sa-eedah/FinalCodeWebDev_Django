from django.contrib import admin
from .models import Category, Item
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_by', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
