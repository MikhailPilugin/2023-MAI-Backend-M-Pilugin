from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
#from django.shortcuts import render
from django.views import View
#from catalog import serializers
from django.core.serializers import serialize
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
import json


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


def get_all(request: HttpRequest) -> HttpResponse:
    def __authors__(authors):
        data = []
        for author in authors:
            data.append(author.to_json())
        return data

    return HttpResponse(
        JsonResponse({
            "authors": __books__(Author.objects.all()),
            "books": __authors__(Book.objects.all())
        })
    )


def search_book(request: HttpRequest) -> HttpResponse:
    title = request.GET.get("title")
    if title is None:
        return HttpResponseBadRequest(JsonResponse("Title parameter is required"))

    books = Book.objects.filter(title__icontains=title)
    obj = {"content": __books__(books)}
    return HttpResponse(JsonResponse(obj))

def __books__(books):
    data = []
    for book in books:
        data.append(book.to_json())
    return data

def __authors__(authors):
    data = []
    for author in authors:
        data.append(author.to_json())
    return data
