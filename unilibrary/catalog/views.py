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

def add_author(request: HttpRequest) -> HttpResponse:
    def __body__(request: HttpRequest):
        body_unicode = request.body.decode('utf-8')
        return json.loads(body_unicode)
    body = __body__(request)
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    birth_date = body.get('birth_date')
    death_date = body.get('death_date')

    if first_name is None:
        return HttpResponseBadRequest(JsonResponse("Missing first_name"))
    elif last_name is None:
        return HttpResponseBadRequest(JsonResponse("Missing last_name"))
    elif birth_date is None:
        return HttpResponseBadRequest(JsonResponse("Missing birth_date"))

    author = Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        death_date=death_date
    )
    return HttpResponse(JsonResponse({"id": str(author.id)}))

def add_book(request: HttpRequest) -> HttpResponse:
    def __body__(request: HttpRequest):
        body_unicode = request.body.decode('utf-8')
        return json.loads(body_unicode)
    author_id = request.GET.get("author_id")
    body = __body__(request)
    title = body.get('title')
    publication_date = body.get('publication_date')

    if author_id is None:
        return HttpResponseBadRequest(JsonResponse("Missing author_id"))
    elif title is None:
        return HttpResponseBadRequest(JsonResponse("Missing title"))
    elif publication_date is None:
        return HttpResponseBadRequest(JsonResponse("Missing publication_date"))

    author = Author.objects.get(pk=author_id)
    if author is None:
        return HttpResponseBadRequest(JsonResponse("Missing author with id = " + str(author_id)))

    book = Book.objects.create(
        title=title,
        author=author,
        publication_date=publication_date,
    )
    return HttpResponse(JsonResponse({"id": str(book.id)}))

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
