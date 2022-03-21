from django.contrib import admin

from .models import Movies, Ratings
# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'release_date', 'price']
admin.site.register(Movies, MoviesAdmin)

class RatingAdmin(admin.ModelAdmin):
    fields = ['rating', 'rated_by', 'movieID']
admin.site.register(Ratings, RatingAdmin)
