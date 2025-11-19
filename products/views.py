from django.shortcuts import render, get_object_or_404, redirect
from products.models import Products  # Assuming your product model is named 'Products'
from products.forms import AddProductsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages

# Helper function to check if a user is an admin
def is_admin(user):
    return user.is_superuser

# --- Core Views ---

def home_view(request):
    # This view is called from the traceback, serves the main index page.
    # Assumed logic: fetch a few products to display on the home page.
    try:
        featured_products = Products.objects.all().order_by('-product_id')[:4]
    except:
        featured_products = []
        
    context = {'featured_products': featured_products}
    return render(request, 'index.html', context)

def products_view(request):
    # This view displays all products
    context = {'products': Products.objects.all()}
    return render(request, 'products.html', context)

def productdetails_view(request, pk):
    # This view displays a single product's details
    product = get_object_or_404(Products, product_id=pk)
    context = {'product': product}
    return render(request, 'product-details.html', context)

# --- Cart Views ---

def add_to_cart(request, product_id):
    """
    Handles adding an item to the cart or changing its quantity/removing it.
    """
    product_id_str = str(product_id)
    cart = request.session.get('cart', {})
    
    if request.method == 'POST':
        action = request.POST.get('action')
        quantity_to_add = int(request.POST.get('quantity', 1))

        product = get_object_or_404(Products, product_id=product_id)

        if action:
            # Logic for changing quantity or removing item from cart
            if product_id_str in cart:
                current_quantity = cart[product_id_str]

                if action == 'increase':
                    cart[product_id_str] = current_quantity + 1
                    messages.success(request, f"Increased quantity of {product.product_name} in your cart.")
                
                elif action == 'decrease':
                    if current_quantity > 1:
                        cart[product_id_str] = current_quantity - 1
                        messages.info(request, f"Reduced quantity of {product.product_name} in your cart.")
                    else:
                        # Quantity is 1, so remove the item entirely
                        del cart[product_id_str]
                        messages.warning(request, f"{product.product_name} was removed from your cart.")
        
        else:
            # Initial add from product-details page
            if product_id_str in cart:
                cart[product_id_str] += quantity_to_add
                messages.success(request, f"Updated quantity of {product.product_name} in your cart.")
            else:
                cart[product_id_str] = quantity_to_add
                messages.success(request, f"{product.product_name} added to your cart.")
        
        request.session['cart'] = cart
        request.session.modified = True
            
    return redirect('cart')

# 🌟 NEW VIEW TO FIX THE NOREVERSEMATCH ERROR 🌟
def cart_view(request):
    """
    Displays the contents of the shopping cart by retrieving product details 
    from the database based on session data.
    """
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0

    # Fetch product details for items in the cart
    for product_id_str, quantity in cart.items():
        try:
            # Assumes product_id is an integer field
            product = Products.objects.get(product_id=int(product_id_str))
            
            subtotal = product.product_price * quantity
            grand_total += subtotal
            
            # Populate the list with all details needed for cart.html
            cart_items.append({
                'product_id': product.product_id,
                'product_name': product.product_name,
                'product_price': product.product_price,
                'product_image_url': getattr(product, 'product_image_url', ''), # Use getattr for safety
                'product_image': getattr(product, 'product_image', None), # Use getattr for safety
                'quantity': quantity,
                'subtotal': subtotal
            })
        except Products.DoesNotExist:
            # Clean up the session if a product no longer exists
            if product_id_str in request.session['cart']:
                del request.session['cart'][product_id_str]
                request.session.modified = True
            continue

    context = {
        'cart_items': cart_items,
        'grand_total': grand_total,
    }
    
    return render(request, 'cart.html', context)


# --- Admin Views ---

@login_required
@user_passes_test(is_admin)
def addproducts_views(request):
    context = {}
    submitted = False
    
    if request.method == "POST":
        form = AddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add-products') + '?submitted=True')
        else: 
            # Original code printed errors, now passing them in context
            context = {'errors' : form.errors, 'form': form}
            return render(request, 'add_products.html', context)
    else:
        form = AddProductsForm()
        if 'submitted' in request.GET:
            submitted = True

        context = {'form' : form, 'submitted' : submitted}
    return render(request, 'add_products.html', context)


@login_required
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    # Retrieve the count of all products from the database model
    total_products = Products.objects.count()
    context = {
        'total_products': total_products,
        # Placeholder for other dashboard data...
    }
    return render(request, 'admin_dashboard.html', context)

# --- Search View ---

def search_results(request):
    """
    Handles search queries and displays matching products.
    """
    query = request.GET.get('q')
    if query:
        # Search in product name or details (case-insensitive)
        products = Products.objects.filter(
            Q(product_name__icontains=query) | 
            Q(product_details__icontains=query)
        )
    else:
        products = Products.objects.all() # Or an empty queryset, depending on desired behavior
        
    context = {'products': products, 'query': query}
    return render(request, 'products.html', context)