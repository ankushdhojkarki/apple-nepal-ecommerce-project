from django.urls import path, include
# Import the new cart_view function here
from .views import products_view, productdetails_view, addproducts_views, search_results, add_to_cart, admin_dashboard_view, cart_view


urlpatterns = [

    path('products-views/', products_view, name = 'products'),
    path('product-details/<int:pk>', productdetails_view, name = 'product-details'),
    path('add_products/', addproducts_views, name = 'add-products'),
    path('search/', search_results, name ='search'), 
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    
    # 🌟 NEW CART VIEW PATH (Resolves the NoReverseMatch error)
    path('cart/', cart_view, name='cart'),

    # NEW ADMIN DASHBOARD PATH
    path('admin-dashboard/', admin_dashboard_view, name='admin-dashboard'),

]