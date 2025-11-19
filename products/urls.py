
from django.urls import path, include
from .views import   products_view, productdetails_view, addproducts_views, search_results, add_to_cart, cart_view, remove_from_cart, update_cart_quantity


urlpatterns = [

    path('products-views/', products_view, name = 'products'),
    path('product-details/<int:pk>', productdetails_view, name = 'product-details'),
    path('add_products/', addproducts_views, name = 'add-products'),
    path('search/', search_results, name ='search'), 
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('cart/', cart_view, name='cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('update-cart/<int:product_id>/', update_cart_quantity, name='update-cart'),

]  

 

