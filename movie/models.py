from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    STATUS_CHOICES = (
        ('Movie', 'Movie'),
        ('Tv-series', 'Tv Series'),
        ('Anime', 'Anime'),
    )
    WATCH_CHOICES = (
        ('Watched', 'Watched'),
        ('To watch', 'To watch'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=15,
                            choices=STATUS_CHOICES,
                            default='')
    watch = models.CharField(max_length=20,
                             choices=WATCH_CHOICES)
    year = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(max_length=10, null=False)
    review = models.TextField(null=True, blank=True)
    img_url = models.TextField(default='https://betravingknows.com/wp-content/uploads/2017/'
                                       '06/video-movie-placeholder-image-grey.png')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

