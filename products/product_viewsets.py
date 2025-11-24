from rest_framework import viewsets
from products.models import Products
from products.product_serializers import ProductsSerializer


# ViewSets define the view behavior.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer