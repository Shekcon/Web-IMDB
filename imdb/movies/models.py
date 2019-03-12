from django.db import models

# Create your models here.
class Actors(models.Model):
    GENDER = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER'),
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthdate = models.DateField()
    sex = models.CharField(max_length=6,choices=GENDER, default='male')
    nationality = models.CharField(max_length=150)
    is_alive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_name +" " + self.last_name


class Movies(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=False)
    release_date = models.DateField()
    # category = models. 
    # actors = models.
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

class Awards(models.Model):
    pass