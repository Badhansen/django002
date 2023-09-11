from django.urls import path
from .views import PostListAPIView, PostDetailAPIView


urlpatterns = [
    path('<int:pk>/', PostDetailAPIView.as_view()),    
    path('', PostListAPIView.as_view()),
]