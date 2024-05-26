from django.db import models

# Create your models here.
class Movies(models.Model):
    MovieTitle = models.TextField()
    Location =models.URLField()

class AnimationAnime(models.Model):
    AnimTitle = models.TextField()
    Location =models.URLField()
   

class Serie(models.Model):
    SeriesTitle = models.TextField()
    Location =models.URLField()
   


class Movie(models.Model):
    MovieTitle = models.TextField()
    Location =models.URLField()
