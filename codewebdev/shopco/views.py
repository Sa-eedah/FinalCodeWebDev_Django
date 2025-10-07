from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    # Example filters (you can adjust to your actual model fields)
    new_arrivals = Product.objects.all()[:4]  # first 4 products
    top_selling = Product.objects.order_by('-price')[:4]  # top 4 by price

    context = {
        'new_arrivals': new_arrivals,
        'top_selling': top_selling,
    }
    return render(request, 'shopco/index.html', context)

def filter_page(request):
    query = request.GET.get('q')  # Get the search query from ?q=
    products = []

    if query:
        # Filter products by name or brand (case-insensitive)
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(brand__icontains=query)

    return render(request, "shopco/filter.html", {
        "query": query,
        "products": products
    })

