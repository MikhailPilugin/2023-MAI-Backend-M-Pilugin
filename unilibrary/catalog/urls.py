from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path("api//", get_all, name="get-all"),
    path('api/authors/', AuthorView.as_view()),
    path('api/authors/<int:pk>/', AuthorProcessing.as_view(), name='author-processing'),
    path('api/books/', BookView.as_view()),
    path('api/books/<int:pk>/', BookProcessing.as_view(), name='book-processing'),
    path("api/book/search", search_book, name="search-book"),
    path("api/book/create", add_book, name="add-book"),
    path("api/author/create", add_author, name="add-author"),
]
