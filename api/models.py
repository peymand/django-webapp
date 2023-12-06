# from tastypie.resources import ModelResource

from movies.models import Movie


# Create your models here.
class MovieResource():
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
