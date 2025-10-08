from django.shortcuts import render, get_object_or_404
from item.models import Item, Category

def dashboard_index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'dashboard/index.html', {
        'items': items, 
        'categories': categories})

def dashboard_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'dashboard/detail.html', {
        'item': item})
