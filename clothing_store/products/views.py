from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request, 'products/index.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product.html', {'product': product})

