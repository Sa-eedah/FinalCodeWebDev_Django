from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'original_price', 'rating', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'original_price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'rating': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'step': '0.1',
                'min': '0',
                'max': '5'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'original_price', 'rating', 'image', 'is_sold',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'original_price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'rating': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'step': '0.1',
                'min': '0',
                'max': '5'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }