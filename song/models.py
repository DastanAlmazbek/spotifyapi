from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=True, blank=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        ordering = ['-id']

