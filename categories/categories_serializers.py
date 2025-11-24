from rest_framework import serializers
from categories.models import Categories



class CategoriessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'