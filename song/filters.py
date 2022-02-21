from django_filters import rest_framework as filters
from .models import Song


class SongFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Song
        fields = ['title', 'author']
    
