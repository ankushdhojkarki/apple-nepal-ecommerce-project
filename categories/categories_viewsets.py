from rest_framework import viewsets
from categories.categories_serializers import CategoriessSerializer
from categories.models import Categories



class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriessSerializer
