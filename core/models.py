from pyexpat import model
from django.db import models
from django.db.models import Avg, Count


# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)
    release_date = models.DateField()
    price = models.FloatField()
    rating = models.ForeignKey('Ratings', on_delete=models.SET_DEFAULT, default = "NA", null=True)

    def avgRating(self):
        rating = Ratings.objects.filter(movieID=self).aggregate(avarage=Avg('rating'))
        avg = 0
        if rating['avarage'] is not None:
            avg = float(rating['avarage'])
        return avg
        
    def countRating(self):
        rating = Ratings.objects.filter(movieID=self).aggregate(count=Count('rating'))
        count = 0
        if rating['count'] is not None:
            count = int(rating['count'])
        return count

class Ratings(models.Model):
    rating = models.IntegerField()
    rated_by = models.IntegerField()
    movieID = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True)

class MovieInfo(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    director = models.CharField(max_length=200, null=True)

    