from django.shortcuts import render, get_object_or_404
from products.models import Products
from products.forms import AddProductsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)

def addproducts_views(request):
    context = {}
    submitted = False
    print(request.POST)
    if request.method == "POST":
        form = AddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add-products') + '?submitted=True')
        else:
            print(form.errors)     
            return render(request, 'add_products.html', context= {'errors' : form.errors})
    else:
        form = AddProductsForm()
        if 'submitted' in request.GET:
            submitted = True

        context = {'form' : form, 'submitted' : submitted}
    return render(request, 'add_products.html', context)


def products_view(request):
    context = {'products': Products.objects.all()}
    return render(request, 'products.html', context)

def productdetails_view(request, pk):
    product_id_value = request.GET.get('id')
    product = get_object_or_404(Products, product_id=pk)
    context = {'product':product}
    return render(request, 'product-details.html', context)

def search_results(request):
    query = request.GET.get('q')
    products = Products.objects.all()

    if query:
        products= Products.objects.filter(
            Q(product_name__icontains=query) |
            Q(product_details__icontains=query) |
            Q(category__category_name__icontains=query)
        ).distinct()

    context = {
        'query':query,
        'products':products,
        'result_count':products.count(),
    }

    return render(request, 'products.html', context)


