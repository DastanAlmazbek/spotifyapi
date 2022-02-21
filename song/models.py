from pyexpat import model
from django.db import models
from account.models import User


class Song(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=True, blank=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        ordering = ['-id']


class SongReview(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    is_liked = models.BooleanField(default=False, null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-id']    


class SongFavorite(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="favourites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")
    favorite = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']