from django.db import models
from .product_model import product
from .store_model import store

# Create your models here.

class store_product(models.Model):
    store = models.ForeignKey(store, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    price  = models.IntegerField(default=0)
    amount  = models.IntegerField(default=1)

