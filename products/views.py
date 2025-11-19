from django.shortcuts import render, get_object_or_404, redirect
from products.models import Products
from products.forms import AddProductsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages

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

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Products, product_id = product_id)

        try:
            quantity = int(request.POST.get('quantity',1))
        except ValueError:
            quantity = 1

        cart = request.session.get('cart', {})

        product_id_str = str(product_id)

        if product_id_str in cart:
            cart[product_id_str] += quantity
        else:
            cart[product_id_str] = quantity

        request.session['cart'] = cart
        request.session.modified = True

        messages.success(request, f"{quantity} x {product.product_name} added to your cart.")

    return redirect('product-details', pk=product_id)

def cart_view(request):
    # This function needs your existing logic to prepare cart_items and grand_total
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0
    
    for product_id_str, quantity in cart.items():
        try:
            product = Products.objects.get(product_id=int(product_id_str))
            item_subtotal = product.product_price * quantity
            grand_total += item_subtotal

            cart_items.append({
                'product_id': product.product_id,
                'product_name': product.product_name,
                'product_price': product.product_price,
                # Assuming product_image_url is a field or method on your Products model
                'product_image_url': getattr(product, 'product_image_url', None), 
                'quantity': quantity,
                'item_subtotal': item_subtotal,
            })
        except Products.DoesNotExist:
            # Optionally remove product from cart if it no longer exists in DB
            pass

    context = {
        'cart_items': cart_items,
        'grand_total': grand_total,
    }
    return render(request, 'cart.html', context)


def remove_from_cart(request, product_id):
    if request.method == 'POST':
        product_id_str = str(product_id)
        cart = request.session.get('cart', {})
        
        if product_id_str in cart:
            product = get_object_or_404(Products, product_id=product_id)
            del cart[product_id_str]
            request.session['cart'] = cart
            request.session.modified = True
            messages.warning(request, f"{product.product_name} was removed from your cart.")
            
    return redirect('cart')


def update_cart_quantity(request, product_id):
    if request.method == 'POST':
        product_id_str = str(product_id)
        cart = request.session.get('cart', {})
        action = request.POST.get('action') # 'increase' or 'decrease'
        
        if product_id_str in cart:
            current_quantity = cart[product_id_str]
            product = get_object_or_404(Products, product_id=product_id)

            if action == 'increase':
                cart[product_id_str] = current_quantity + 1
                messages.success(request, f"Increased quantity of {product.product_name} to {current_quantity + 1}.")
            
            elif action == 'decrease':
                if current_quantity > 1:
                    cart[product_id_str] = current_quantity - 1
                    messages.info(request, f"Reduced quantity of {product.product_name} to {current_quantity - 1}.")
                else:
                    # Quantity is 1, so remove the item entirely
                    del cart[product_id_str]
                    messages.warning(request, f"{product.product_name} was removed from your cart.")

            request.session['cart'] = cart
            request.session.modified = True
            
    return redirect('cart')