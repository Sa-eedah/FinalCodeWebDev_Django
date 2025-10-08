from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'title', 'description', 'price', 'original_price',
            'category', 'image', 'rating', 'is_sold'
        ]

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'title', 'description', 'price', 'original_price',
            'category', 'image', 'rating', 'is_sold'
        ]
