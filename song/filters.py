from django_filters import rest_framework as filters
from .models import Song


class SongFilter(filters.FilterSet):
    title = filters.CharFilter()
    genre = filters.CharFilter()
    author = filters.CharFilter()

    class Meta:
        model = Song
        fields = '__all__'