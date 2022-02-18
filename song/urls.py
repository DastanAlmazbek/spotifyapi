from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view()),
]