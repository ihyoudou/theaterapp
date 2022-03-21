from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Movies

# Create your views here.

def index(request):
    return HttpResponse('hello world')

def movieInfo(request, id):
    movie = Movies.objects.get(pk=id)
    
    context = {
        'movie': movie
    }
    return render(request, 'details.html', context)