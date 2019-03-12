from django import forms

from .models import Movies, Actors

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = "__all__"


class ActorForm(forms.ModelForm):

    class Meta:
        model = Actors
        fields = "__all__"