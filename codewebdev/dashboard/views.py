from django.shortcuts import render
from .models import Item, Category

def dashboard(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'dashboard/dashboard.html', {
        'items': items,
        'categories': categories,
    })

