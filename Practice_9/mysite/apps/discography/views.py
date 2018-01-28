from django.shortcuts import render
from django.http import Http404

from .models import Song, Musician, Genre
from .forms import MusicianSortingForm


def get_discography(request):
    discography_list = []

    for musician in Musician.objects.all():
        for song in Song.objects.filter(musician__name=musician).order_by('musician',
                                                                          'album',
                                                                          'name'):
            temp_dict = {"musician" : song.musician,
                         "album" : song.album,
                         "song" : song.name}
            discography_list.append(temp_dict)

    output_data = {"discography_list" : discography_list}

    return render(request,
                  'discography/discography.html',
                  output_data)


def get_musician_list(request):
    form = MusicianSortingForm(request.GET)
    musicians = Musician.objects.all()

    if form.is_valid():
        if form.cleaned_data["ordering"]:
            musicians = musicians.order_by(form.cleaned_data["ordering"])

    output_data = {"musicians" : musicians,
                   "form" : form}

    return render(request,
                  'discography/musicians.html',
                  output_data)


def get_songs_by_musician(request, arg_musician):
    try:
        musician = Musician.objects.get(name=arg_musician)
    except Musician.DoesNotExist:
        raise Http404

    info = musician.information
    output_data = {"musician" : musician,
                   "info": info,
                   "songs" : musician.musician_songs.all().order_by("name")}

    return render(request,
                  "discography/songs_by_musician.html",
                  output_data)


def get_songs_by_genre(request, arg_genre):
    try:
        genre = Genre.objects.get(name=arg_genre)
    except Genre.DoesNotExist:
        raise Http404

    output_data = {"genre" : genre,
                   "songs" : genre.genre_songs.all().order_by("name")}

    return render(request,
                  "discography/songs_by_genre.html",
                  output_data)