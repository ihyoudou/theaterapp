from pyexpat import model
from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)
    release_date = models.DateField()
    price = models.FloatField()