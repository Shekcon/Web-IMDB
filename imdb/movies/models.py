from django.db import models

# Create your models here.


class Actors(models.Model):
    GENDER = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER'),
    )
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    birthdate = models.DateField(blank=False)
    sex = models.CharField(max_length=6, choices=GENDER, default='male')
    nationality = models.CharField(max_length=150, blank=False)
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Categories(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    release_date = models.DateField(blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actors, blank=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


class Awards(models.Model):
    # name = models.CharField(max_length=150, blank=False)
    # kind = models.

    def __str__(self):
        return self.name
