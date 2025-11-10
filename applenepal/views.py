from django.shortcuts import render, get_object_or_404
from products.models import Products 
from django.http import Http404
from categories.models import Categories


# View Functions

def home_view(request):
    context = {'featured_products': Products.objects.all().order_by('product_id')[:4] } 
    return render(request, 'index.html', context)

def categories_view(request):
    context = {'categories': Categories.objects.all()}
    return render(request, 'categories.html', context)


def products_view(request):
    print('***', request.GET)
    # This view will pass ALL products. You can add filtering here later!
    category_id = request.GET.get('category')
    all_products = Products.objects.all()
    if category_id and category_id.isdigit():
        all_products = all_products.filter(category_id = int(category_id)) 
    context = {'products': all_products}
    return render(request, 'products.html', context)

def productdetails_view(request):
    product_id_str = request.GET.get('id')  

    if not product_id_str or not product_id_str.isdigit():
        raise Http404("Product ID is missing or invalid.")

    
    product_id = int(product_id_str)
    product = get_object_or_404(Products, product_id=product_id)

    context = {'product': product}
    return render(request, 'product-details.html', context) 