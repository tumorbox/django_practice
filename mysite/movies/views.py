from django.shortcuts import render, redirect, get_object_or_404
import requests


from .models import Movie
from .forms import MovieForm

# Create your views here.
def movies(request):
    movie = Movie.objects.all()
    context = {
        'movies' : movie
    }
    return render(request, 'movies/movie.html', context)

def form(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:movies')
    else:
        form = MovieForm()
    context = {
        'form':form
    }
    return render(request, 'movies/form.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:movies')
    else:
        form = MovieForm(instance=movie)
    context = {
        'form' : form
    }
    return render(request, 'movies/form.html', context)

def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return redirect('movies:movies')