from django.db import models

# Create your models here.

class store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    open_time  = models.TimeField()


    def __str__(self):
        return self.name