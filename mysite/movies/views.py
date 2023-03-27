from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    context = {
        'title': 'Фильмы',
        'movies': Movie.objects.all(),
        'actors': Actor.objects.all(),
        'producers': Producer.objects.all()
    }
    return render(request, 'movies/index.html', context)
