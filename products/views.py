from django.shortcuts import render, get_object_or_404
from products.models import Products
from products.forms import AddProductsForm
from django.http import HttpResponseRedirect

# Create your views here.
def addproducts_views(request):
    submitted = False
    if request.method == "POST":
        form = AddProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_products/?submitted=True')
    else:
        form = AddProductsForm()
        if 'submitted' in request.GET:
            submitted = True

        context = {'form' : form, 'submitted' : submitted}
    return render(request, 'add_products.html', context)


def products_view(request):
    context = {'products': Products.objects.all()}
    return render(request, 'products.html', context)

def productdetails_view(request):
    product_id_value = request.GET.get('id')
    product = get_object_or_404(Products, product_id=product_id_value)
    context = {'product':product}
    return render(request, 'product-details.html', context)


