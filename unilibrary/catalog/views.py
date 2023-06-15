from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
#from catalog import serializers
from django.core.serializers import serialize
# from .serializers import AuthorSerializer, BookSerializer, BookInstanceSerializer, GenreSerializer

from catalog.models import Author, Book

class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()

        authors_serialized_data = serialize('python', authors)

        data = {
            'authors': authors_serialized_data,
        }

        if request.method == "GET":
            return JsonResponse(data)
        
        
class BookView(View):
    def get(self, request):
        books = Book.objects.all()

        books_serialized_data = serialize('python', books)

        data = {
            'books': books_serialized_data,
        }
        return JsonResponse(data)