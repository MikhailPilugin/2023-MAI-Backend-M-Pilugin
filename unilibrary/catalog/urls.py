from django.urls import path
from . import views
from .views import AuthorView, BookView, AuthorProcessing, BookProcessing, get_all


urlpatterns = [
    path("api//", get_all, name="get-all"),
    path('api/authors/', AuthorView.as_view()),
    path('api/authors/<int:pk>/', AuthorProcessing.as_view(), name='author-processing'),
    path('api/books/', BookView.as_view()),
    path('api/books/<int:pk>/', BookProcessing.as_view(), name='book-processing'),
]
