from django.contrib import admin
from .models import Actors, Movies, Categories
# Register your models here.


admin.site.register(Actors)
admin.site.register(Movies)
admin.site.register(Categories)