from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movie1 = Movie()
    movie1.name = 'X-MAN'
    movie1.comments = 112
    movie1.image = 'movie1.jpg'
    movie2 = Movie()
    movie2.name = 'SPIDER MAN 2'
    movie2.comments = 7
    movie2.image = 'movie2.jpg'
    movie3 = Movie()
    movie3.name = 'SPIDER MAN 3'
    movie3.comments = 24
    movie3.image = 'movie3.jpg'

    movies = [movie1, movie2, movie3]


    template_name = 'movie_app/index.html'
    context = {'movies': movies}
    return render(request, template_name, context)