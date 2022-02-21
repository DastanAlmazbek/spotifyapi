from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Song, SongReview, SongFavorite
from .serializers import SongSerializer, SongReviewSerializer, SongFavoriteSerializer
from .filters import SongFilter
from rest_framework.pagination import PageNumberPagination  


class ListCreateSongAPIView(ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SongFilter
    pagination_class = PageNumberPagination

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
