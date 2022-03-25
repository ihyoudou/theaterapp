from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.movieDetails, name="movieDetails"),
    path('search', views.search, name="search"),
    path('api/buyTicket', views.buyMovieTicket, name="buyMovieTicket"),
    path('api/rateMovie', views.rateMovie, name="rateMovie")
]