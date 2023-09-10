from django.urls import path
from .views import BookAPIView, BookDetailAPIView


urlpatterns = [
    path('<int:pk>/', BookDetailAPIView.as_view()),
    path('', BookAPIView.as_view()),
]