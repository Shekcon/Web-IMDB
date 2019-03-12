from django.shortcuts import render, reverse
from .forms import MovieForm

def index(request):
    contents = {
        "user": request.user,
        "form": MovieForm()
    }
    return render(request, 'movies/index.html', contents)


def view_actors(request):
    return render(request, 'movies/actors.html')


def view_awards(request):
    return render(request, 'movies/awards.html')