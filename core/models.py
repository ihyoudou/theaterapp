from pyexpat import model
from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)
    release_date = models.DateField()
    price = models.FloatField()

class Ratings(models.Model):
    rating = models.IntegerField()
    rated_by = models.IntegerField()
    movieID = models.ForeignKey(Movies, on_delete=models.CASCADE)
    