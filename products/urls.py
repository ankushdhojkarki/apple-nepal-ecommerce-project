
from django.urls import path
from .views import   products_view, productdetails_view

urlpatterns = [

    path('products-views/', products_view, name = 'products'),
    path('product-details/', productdetails_view, name = 'product-details'),

]  

 

