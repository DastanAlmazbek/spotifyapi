from django.contrib import admin
from .models import Song, SongFavorite, SongReview

admin.site.register(Song)
admin.site.register(SongReview)
admin.site.register(SongFavorite)
