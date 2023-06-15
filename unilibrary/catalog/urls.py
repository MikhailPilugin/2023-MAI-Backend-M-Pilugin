from django.urls import path
from . import views
from .views import AuthorView, BookView 


urlpatterns = [
    path('authors/', AuthorView.as_view()),
    #path('authors/<int:pk>/', AuthorProcessing.as_view(), name='author-processing'),
    path('books/', BookView.as_view()),
    #path('books/', BookAdd.as_view(), name='book-add'),
]
