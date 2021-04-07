from django.shortcuts import render, get_object_or_404
from .models import Products


def product(request):
    all_products = Products.objects
    return render(request, 'product/category.html', {'all_products': all_products})


def cart(request, product_id):
    carts = get_object_or_404(Products, pk=product_id)
    return render(request, 'product/cart.html', {'carts': carts})
