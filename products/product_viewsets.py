from rest_framework import viewsets , filters
from products.models import Products
from products.product_serializers import ProductsSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# ViewSets define the view behavior.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class StandardResultsSetPAgination(PageNumberPagination):
    page_size= 10
    page_size_query_param = 'limit'
    max_page_size = 100


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = StandardResultsSetPAgination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['product_name']
    ordering_fields = ['product_id', 'product_name']