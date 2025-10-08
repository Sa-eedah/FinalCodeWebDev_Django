from django.contrib import admin
from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_count')
    search_fields = ('name',)
    
    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Number of Items'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'original_price', 'rating', 'is_sold', 'created_by', 'created_at')
    list_filter = ('is_sold', 'category', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_sold',)
    readonly_fields = ('created_at', 'discount_percentage')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'description', 'image')
        }),
        ('Pricing', {
            'fields': ('price', 'original_price', 'discount_percentage')
        }),
        ('Rating & Status', {
            'fields': ('rating', 'is_sold')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def discount_percentage(self, obj):
        return f"{obj.discount_percentage}%"
    discount_percentage.short_description = 'Discount'