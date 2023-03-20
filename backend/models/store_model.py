from django.db import models

# Create your models here.

class store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100, unique=True)
    open_time  = models.TimeField(default='08:00')
    close_time  = models.TimeField(default='22:00')


    def __str__(self):
        return self.name