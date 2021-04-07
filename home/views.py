from django.shortcuts import render
from .models import Product_home


def home(request):
    products = Product_home.objects
    return render(request, 'home/home.html', {'products': products})
