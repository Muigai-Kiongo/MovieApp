from django.shortcuts import render
from .models import *

# Create your views here.
def HomeFragment(request):
    return render(request, "index.html")


def MoviesFragment(request):
    return render (request, "./layouts/movies/movies.html")
    ...


def SeriesFragment(request):
    return render (request, "./layouts/series/series.html")
    ...


def AnimFragment(request):
    return render (request, "./layouts/animations/anim.html")
    ...