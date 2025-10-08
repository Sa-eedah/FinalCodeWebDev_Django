from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="items")
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    rating = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def discount_percentage(self):
        """Calculate discount percentage if original_price exists"""
        if self.original_price and self.original_price > self.price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return round(discount)
        return 0
