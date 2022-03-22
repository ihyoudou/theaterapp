from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Movies, Ratings
from userAccount.models import Orders
import json
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

@login_required
def rateMovie(request):

    body = json.loads(request.body)
    if body:
        if request.user:
            rate = body['rate']
            movie = Movies.objects.get(pk=body['movieID'])

            print(Ratings.objects.filter(rated_by=request.user.id, movieID=movie))
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
        return JsonResponse({'success': False, 'reason': 'not a POST request'})
@login_required
def buyMovieTicket(request, id):

    try:
        movie = Movies.objects.get(pk=id)
        user = User.objects.get(id=request.user.id)
        if request.POST:
            order = Orders()
            order.ordered_by = user
            order.item = movie
            order.price = movie.price
            order.save()
            messages.success(request, "Order was successful!")
            return redirect("core:index")

        else:
            context = {
                'title': "Buy ticket",
                'desc': "Do you want to buy ticket for {}?".format(movie.title),
                'buttonText': "Yes",
                'ticket_price': movie.price
            }
            return render(request, 'form.html', context)

    except ObjectDoesNotExist as err:
        return HttpResponse("not found")