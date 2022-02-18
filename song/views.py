import imp
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Song
from .serializers import SongSerializer
from .filters import SongFilter
from rest_framework.pagination import PageNumberPagination

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SongFilter
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save()


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]
