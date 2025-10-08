from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    
    @property
    def discount_percentage(self):
        """Calculate discount percentage if original_price exists"""
        if self.original_price and self.original_price > self.price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return round(discount)
        return 0