from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def sign_up(request):
    """
    Task:
    - if this is a POST request we need to process the form data
    - create a form instance and populate it with data from the request
    - check whether it's valid
    - if a GET (or any other method) we'll create a blank form
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # working on this shit
            return HttpResponseRedirect(redirect('movies:home'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    return


def logout(request):
    return
