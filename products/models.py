from django.db import models
from categories.models import Categories

# Create your models here.
class Products(models.Model):
    product_image = models.URLField(max_length = 500)
    product_name = models.CharField(max_length = 255)
    product_id = models.AutoField(primary_key=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_details = models.CharField(max_length = 5000)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE, related_name= 'products', null = True)
    
    def __str__(self):
        return self.product_name
    