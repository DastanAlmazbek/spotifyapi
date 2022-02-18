from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['-id']

