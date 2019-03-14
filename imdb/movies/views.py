from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect
from .forms import MovieForm, ActorForm
from .models import Movies, Actors
from django.contrib.auth.decorators import login_required
from .models import Comments
from django.contrib.contenttypes.models import ContentType


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
    kind_type = ContentType.objects.get(model='movies')
    if request.method == "POST":
        Comments.objects.create(text=request.POST['comment'],
                                author=request.user,
                                content_type=kind_type,
                                object_id=movie.id)
    comments = Comments.objects.filter(content_type=kind_type, object_id=movie.id).order_by('-date')
    
    contents = {
        "movie": movie,
        "actors": ", ".join(map(str,movie.actors.all())),
        "comments": comments,
        "user": str(request.user)
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


@login_required
def update_comment(request):
    print(request.POST['form_url'])
    return HttpResponseRedirect(request.POST['request_url'])

@login_required
def delete_comment(request, id):
    # comment = Comments.objects.get(id=id)
    # comment.delete()
    print(request.POST)
    # return HttpResponseRedirect(request.POST['request_url'])
