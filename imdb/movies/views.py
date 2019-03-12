from django.shortcuts import render, reverse


def index(request):
    return render(request, 'movies/index.html')


def view_actors(request):
    return render(request, 'movies/actors.html')


def view_awards(request):
    return render(request, 'movies/awards.html')