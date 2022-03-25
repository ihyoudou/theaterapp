from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from django.contrib import messages

from .models import Movies, Ratings
from .forms import RatingForm

from userAccount.models import Orders
import json


# Create your views here.

def index(request):
    movies_list = Movies.objects.all()
    paginator = Paginator(movies_list, 10)
    page = request.GET.get('page', 1)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)


    context = {
        'movies': movies
    }
    # return HttpResponse('hello world')
    return render(request, 'index.html', context)

def movieDetails(request, id):

    try:
        movie = Movies.objects.get(pk=id)

        context = {
            'movie': movie,
            'ratingForm': RatingForm()
        }
        return render(request, 'details.html', context)
    except ObjectDoesNotExist as err:
        return HttpResponse("not found")

def search(request):
    if request.POST:
        searchPhrase = request.POST.get('searchphrase')

        context = {
            'movies': Movies.objects.filter(title__icontains=searchPhrase),
            'searchPhrase': searchPhrase
        }
        return render(request, 'index.html', context)
    else:
        return redirect('core:index')

@login_required
def rateMovie(request):

    body = json.loads(request.body)
    # checking if body is present
    # validating user input
    ratingOption = RatingForm({'rating':body['rate']})

    if body and ratingOption.is_valid():
        # checking if user is loged in 
        # (it should be due to @login_required, but just a sanity check)
        if request.user:
            rate = body['rate']
            movie = Movies.objects.get(pk=body['movieID'])
        
            if not Ratings.objects.filter(rated_by=request.user.id, movieID=movie):
                
                rating = Ratings()
                rating.rating = rate
                rating.rated_by = request.user.id
                rating.movieID = movie

                rating.save()

                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'reason': 'this user already rated that movie'})
        else:
            return JsonResponse({'success': False, 'reason':'user is not authenticated'}) 
    else:
        return JsonResponse({'success': False, 'reason': 'not a valid request'})

@login_required
def buyMovieTicket(request):
    body = json.loads(request.body)
    try:
        movie = Movies.objects.get(pk=body['movieID'])
        user = User.objects.get(id=request.user.id)
        if body:
            order = Orders()
            order.ordered_by = user
            order.item = movie
            order.price = movie.price
            order.save()
            
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'reason': 'invalid request'})

    except ObjectDoesNotExist as err:
        return JsonResponse({'success': False, 'reason': 'Movie not found'})