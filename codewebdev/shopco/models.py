from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)
    
    # Default rating of 5.0 — prevents migration errors
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    
    slug = models.SlugField(unique=True)
    
    # Optional timestamps (helpful for sorting/filtering later)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

