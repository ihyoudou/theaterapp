import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theaterapp.settings')

import django
django.setup()

import random
from core.models import Movies
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        movie = Movies()
        movie.title = fakegen.name()
        movie.description = fakegen.text()
        movie.release_date = fakegen.date()
        movie.price = round(random.uniform(10.5, 75.5), 2)

        movie.save()

populate(50)