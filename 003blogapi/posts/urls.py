from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, UserListAPIView, UserDetailAPIView


urlpatterns = [
    path('users/', UserListAPIView.as_view()), # new
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view()),    
    path('', PostListAPIView.as_view()),
]