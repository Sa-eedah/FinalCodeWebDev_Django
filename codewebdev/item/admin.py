from django.contrib import admin
from .models import Item, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'original_price', 'category', 'rating', 'is_sold', 'created_by', 'created_at')
    list_filter = ('is_sold', 'category', 'created_by')
    list_editable = ('price', 'original_price', 'rating', 'is_sold')
    search_fields = ('title', 'description', 'category__name')
    ordering = ('-created_at',)
