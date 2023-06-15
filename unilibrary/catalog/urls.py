from django.urls import path
from . import views
from .views import AuthorView, BookView, AuthorProcessing, BookProcessing


urlpatterns = [
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>/', AuthorProcessing.as_view(), name='author-processing'),
    path('books/', BookView.as_view()),
    path('books/<int:pk>/', BookProcessing.as_view(), name='book-processing'),
]
