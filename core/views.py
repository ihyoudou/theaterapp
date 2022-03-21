from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Movies
from userAccount.models import Orders

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
def buyMovieTicket(request, id):

    try:
        movie = Movies.objects.get(pk=id)
        user = User.objects.get(id=request.user.id)
        if request.POST:
            order = Orders()
            order.ordered_by = user
            order.item = movie
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