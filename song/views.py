from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Song, SongReview, SongFavorite
from .serializers import SongSerializer, SongReviewSerializer, SongFavoriteSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter  


class ListCreateSongAPIView(ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = PageNumberPagination
    search_fields = ['title', 'author']

    def perform_create(self, serializer):
        serializer.save()


class RetrieveUpdateDestroySongAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]


class ListCreateSongReviewAPIView(ListCreateAPIView):
    serializer_class = SongReviewSerializer
    queryset = SongReview.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save()


class ListCreateSongFavoriteAPIView(ListCreateAPIView):
    serializer_class = SongFavoriteSerializer
    queryset = SongFavorite.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save()
