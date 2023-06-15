from django.http import JsonResponse
#from django.shortcuts import render
from django.views import View
#from catalog import serializers
from django.core.serializers import serialize
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics


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

    
class AuthorProcessing(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookProcessing(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer