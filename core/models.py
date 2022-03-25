from pyexpat import model
from django.db import models
from django.db.models import Avg, Count
from datetime import datetime

from userAccount.models import Orders

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)
    release_date = models.DateField()
    price = models.FloatField()

    def avgRating(self):
        rating = Ratings.objects.filter(movieID=self).aggregate(avarage=Avg('rating'))
        avg = 0
        if rating['avarage'] is not None:
            avg = float(rating['avarage'])
        return round(avg, 2)
        
    def countRating(self):
        rating = Ratings.objects.filter(movieID=self).aggregate(count=Count('rating'))
        count = 0
        if rating['count'] is not None:
            count = int(rating['count'])
        return count
        
    def getDirector(self):
        director = MovieInfo.objects.get(movie=self)
        if director:
            return director
        else:
            return False

    def getMovieShowTime(self):
        today = datetime.today()
        dates = MoviePlay.objects.filter(movie=self, date__gte=today)
        if dates:
            return dates
        else:
            return False

    def __str__(self):
        return self.title

class Ratings(models.Model):
    rating = models.IntegerField()
    rated_by = models.IntegerField()
    movieID = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True)

class MovieInfo(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    director = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.movie.title + " info"

class MoviePlay(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    date = models.DateField()
    maxTickets = models.IntegerField()

    def countAvailable(self):
        ordersCount = Orders.objects.filter(item=self).aggregate(count=Count('pk'))
        
        count = self.maxTickets-int(ordersCount['count'])
        return count