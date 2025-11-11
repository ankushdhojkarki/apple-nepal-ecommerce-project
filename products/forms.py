from django import forms
from django.forms import ModelForm
from products.models import Products

#Create a add products form
class AddProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()    
        
        image_file = cleaned_data.get('product_image')
        image_url = cleaned_data.get('product_image_url')

        if image_file and image_url:
            raise forms.ValidationError("Please provide either an image file or an image URL, but not both.")
        if not image_file and not image_url:
            raise forms.ValidationError("You must provide either an image file or an external image URL.")
        
        return cleaned_data