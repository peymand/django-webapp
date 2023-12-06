from django.http import Http404
from django.shortcuts import render

from .models import Movie


# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # SELECT * FROM MOVIES_MOVIE

    # output = ', '.join([m.title for m in movies])

    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'movies/detail.html', {'movie': movie})
    except Movie.DoesNotExist:
        raise Http404()