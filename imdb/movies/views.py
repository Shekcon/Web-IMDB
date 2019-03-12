from django.shortcuts import render, reverse
from .forms import MovieForm, ActorForm
from .models import Movies, Actors


def index(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = MovieForm()
    contents = {
        "user": request.user,
        "form": form,
        "movies_user": Movies.objects.all()
    }
    return render(request, 'movies/index.html', contents)

def view_movie(request, id):
    
    # return render(request, 'movies/actors.html', contents)
    return 


def view_actors(request):
    if request.method == 'POST':
        form = ActorForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = ActorForm()
    contents = {
        "user": request.user,
        "form": form,
        "actors_user": Actors.objects.all()
    }
    return render(request, 'movies/actors.html', contents)


def view_awards(request):
    return render(request, 'movies/awards.html')