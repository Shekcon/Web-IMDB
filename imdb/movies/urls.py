from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.index, name='home'),
    path('actors/', views.view_actors, name='actors'),
    path('awards/', views.view_awards, name='awards'),
]