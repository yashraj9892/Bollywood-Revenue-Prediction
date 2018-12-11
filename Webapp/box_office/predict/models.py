from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    movie_year = ((str(x),str(x)) for x in range(2000,2021))
    movie_runtime = (('0-90','0-90'),
                     ('90-120','90-120'),
                     ('120-150','120-150'),
                     ('150-180','150-180'),
                     ('180+','180+'))
    movie_name = models.CharField(max_length=500)
    genre = models.CharField(max_length=300)
    star_cast = models.CharField(max_length=300)
    director = models.CharField(max_length=500)
    budget = models.CharField(max_length=500)
    year = models.CharField(max_length=4, choices=movie_year, default='2018')
    runtime = models.CharField(max_length=50,choices=movie_runtime,default='0-90')
    

    
