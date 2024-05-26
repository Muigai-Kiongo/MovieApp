from django.urls import path
from . import views

urlpatterns=[
    path("home/",views.HomeFragment),
    path("movies/",views.MoviesFragment),
    path("anim/",views.AnimFragment),
    path("series/",views.SeriesFragment),
]
