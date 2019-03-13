from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect
from .forms import MovieForm, ActorForm
from .models import Movies, Actors
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = MovieForm()
    contents = {
        "form": form,
        "movies_user": Movies.objects.all()
    }
    return render(request, 'movies/index.html', contents)


@login_required
def view_movie(request, id):
    movie = get_object_or_404(Movies, id=id)
    contents = {
        "movie": movie,
        "actors": ", ".join(map(str,movie.actors.all()))
    }
    return render(request, 'movies/view_movie.html', contents)


@login_required
def update_movie(request, id):
    instance = get_object_or_404(Movies, id=id)
    form = MovieForm(request.POST or None,
                     request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movies:home'))
    contents = {
        "movie": Movies.objects.get(id=id),
        "form": form
    }
    return render(request, 'movies/update_movie.html', contents)


@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movies, id=id)
    if request.method == "POST":
        movie.delete()
        return HttpResponseRedirect(reverse('movies:home'))
    contents = {
        "movie": movie
    }
    return render(request, 'movies/delete_movie.html', contents)


@login_required
def view_actor(request, id):
    actor = get_object_or_404(Actors, id=id)
    # print(actor.related.all())
    contents = {
        "actor": actor,
        "movies": ", ".join(map(str, actor.movies_set.all()))
    }
    return render(request, 'movies/view_actor.html', contents)


@login_required
def update_actor(request, id):
    actor = get_object_or_404(Actors, id=id)
    form = ActorForm(request.POST or None,
                     request.FILES or None, instance=actor)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movies:actors'))
    contents = {
        "actor": actor,
        "form": form
    }
    return render(request, 'movies/update_actor.html', contents)


@login_required
def delete_actor(request, id):
    actor = get_object_or_404(Actors, id=id)
    if request.method == "POST":
        actor.delete()
        return HttpResponseRedirect(reverse('movies:actors'))
    contents = {
        "actor": actor
    }
    return render(request, 'movies/delete_actor.html', contents)


@login_required
def view_actors(request):
    if request.method == 'POST':
        form = ActorForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = ActorForm()
    contents = {
        "form": form,
        "actors_user": Actors.objects.all()
    }
    return render(request, 'movies/actors.html', contents)


@login_required
def view_awards(request):
    return render(request, 'movies/awards.html')
