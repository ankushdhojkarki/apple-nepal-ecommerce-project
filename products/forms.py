from django import forms
from django.forms import ModelForm
from products.models import Products

#Create a add products form
class AddProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        