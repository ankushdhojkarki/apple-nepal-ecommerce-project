from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length = 100)
    category_description = models.CharField(max_length = 500, null = True, blank = True)
    category_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.category_name

