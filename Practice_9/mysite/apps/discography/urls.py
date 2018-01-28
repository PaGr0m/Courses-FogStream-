from django.urls import path

from . import views

urlpatterns = [
    path('discography/', views.get_discography),
    path('musicians/', views.get_musician_list),
    path('musicians/<str:arg_musician>/', views.get_songs_by_musician, name='arg_musician'),
    path('genres/<str:arg_genre>/', views.get_songs_by_genre, name='arg_genre'),
]