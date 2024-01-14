from django.shortcuts import render
from .models import Product, ProductCategory

def product_list(reguest):
    products = Product.objects.all()
    return render(reguest, '/product_list.html',{'products':products})