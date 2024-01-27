from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    has_offer=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product_name
