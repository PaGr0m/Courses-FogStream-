from django.contrib import admin
from .models import Album, Genre, Musician, Song


admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Musician)
admin.site.register(Song)