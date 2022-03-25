import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theaterapp.settings')

import django
django.setup()

import random
from core.models import Movies, Ratings, MoviePlay
from faker import Faker
from datetime import datetime, timedelta
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        movie = Movies()
        movie.title = fakegen.name()
        movie.description = fakegen.text()
        movie.release_date = fakegen.date()
        movie.price = round(random.uniform(10.5, 75.5), 2)

        movie.save()

        for entry in range(10):
            rating = Ratings()
            rating.rated_by = 1
            rating.movieID = movie
            rating.rating = random.uniform(1,10)
            rating.save()
        
        for entry in range(5):
            movieplayentry = MoviePlay()
            movieplayentry.movie = movie
            movieplayentry.date = fakegen.date_between_dates(date_start=datetime.now(), date_end=datetime.now() + timedelta(days=14))
            movieplayentry.maxTickets = random.uniform(2,100)
            movieplayentry.save()


populate(40)
