from django.shortcuts import render
from .models import Item

def filter_items(request):
    query = request.GET.get('query')
    products = Item.objects.filter(title__icontains=query) if query else []
    return render(request, 'item/filter.html', {'query': query, 'products': products})
