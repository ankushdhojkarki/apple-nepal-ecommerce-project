
from rest_framework import serializers
from products.models import Products


# Serializers define the API representation.
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'