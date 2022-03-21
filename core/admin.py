from django.contrib import admin

from .models import Movies
# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'release_date', 'price']
admin.site.register(Movies, MoviesAdmin)
