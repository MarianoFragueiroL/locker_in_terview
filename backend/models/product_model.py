from django.db import models

# Create your models here.

class product(models.Model):
    branch = models.CharField(max_length=200)
    product_type = models.CharField(max_length=100)
    calories  = models.FloatField(default=0)
    saturated_fats_percentage = models.FloatField(default=0)
    sugar_percentage = models.FloatField(default=0)


    def __str__(self):
        return self.product_type