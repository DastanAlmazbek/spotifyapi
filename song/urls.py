from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateSongAPIView.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroySongAPIView.as_view()),
]