from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


from .models import Movies

# Create your views here.

def index(request):
    movies = Movies.objects.all()

    context = {
        'movies': movies
    }
    # return HttpResponse('hello world')
    return render(request, 'index.html', context)

def movieDetails(request, id):

    try:
        movie = Movies.objects.get(pk=id)
    
        context = {
            'movie': movie
        }
        return render(request, 'details.html', context)
    except ObjectDoesNotExist as err:
        return HttpResponse("not found")