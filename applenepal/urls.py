"""
URL configuration for applenepal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.contrib.auth.models import User
from products.models import Products
from categories.models import Categories
from rest_framework import routers
from products.product_viewsets import ProductsViewSet
from categories.categories_viewsets import CategoriesViewSet



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'categories', CategoriesViewSet)




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home_view, name = 'home'),
    path('home/', views.home_view, name= 'home'),
    path('categories/', include("categories.urls")),
    path('', include('products.urls')),
    path('products/', include("products.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include("accounts.urls")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
      
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 