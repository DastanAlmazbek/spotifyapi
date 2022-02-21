from django.urls import path, include


from . import views




urlpatterns = [
    path('', views.ListCreateSongAPIView.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroySongAPIView.as_view()),
    path('reviews/', views.ListCreateSongReviewAPIView.as_view())

]
