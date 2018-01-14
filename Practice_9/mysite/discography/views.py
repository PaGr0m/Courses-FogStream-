from django.shortcuts import render
from .models import Song

def get_discography(request):
    # author_linkin = "Linkin Park"
    # linkin = Song.objects.filter(musician__musician__contains="Linkin park").order_by("song")
    songs = Song.objects.all()
    return render(request, 'discography/discography_list.html', {"songs": songs})
