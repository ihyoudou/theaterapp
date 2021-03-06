from django.contrib import admin

from .models import MovieInfo, MoviePlay, Movies, Ratings
from userAccount.models import Orders
# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'release_date', 'price']
admin.site.register(Movies, MoviesAdmin)

class RatingAdmin(admin.ModelAdmin):
    fields = ['rating', 'rated_by', 'movieID']
admin.site.register(Ratings, RatingAdmin)

class OrdersAdmin(admin.ModelAdmin):
    fields = ['ordered_by', 'item', 'price']
    readonly_fields = ['ordered_at']
admin.site.register(Orders, OrdersAdmin)

class MoviesDateAdmin(admin.ModelAdmin):
    fields = ['movie', 'date', 'maxTickets']

admin.site.register(MoviePlay, MoviesDateAdmin)

class MoviesDetailAdmin(admin.ModelAdmin):
    fields = ['director', 'movie']
admin.site.register(MovieInfo, MoviesDetailAdmin)
