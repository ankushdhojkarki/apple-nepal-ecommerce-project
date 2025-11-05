from django.shortcuts import render, get_object_or_404
from products.models import Products

# Create your views here.

def products_view(request):
    context = {'products': Products.objects.all()}
    return render(request, 'products.html', context)

def productdetails_view(request):
    product_id_value = request.GET.get('id')
    product = get_object_or_404(Products, product_id=product_id_value)
    context = {'product':product}
    return render(request, 'product-details.html', context)

  