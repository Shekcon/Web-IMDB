from django.shortcuts import render, reverse
from .forms import MovieForm
from .models import Movies


def index(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST)
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
    return


def view_actors(request):
    return render(request, 'movies/actors.html')


def view_awards(request):
    return render(request, 'movies/awards.html')