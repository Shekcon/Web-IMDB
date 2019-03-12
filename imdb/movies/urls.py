from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.index, name='home'),
    path('movies/<int:id>/', views.view_movie, name='view_movie'),
    path('actors/', views.view_actors, name='actors'),
    path('awards/', views.view_awards, name='awards'),
]