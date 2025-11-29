from rest_framework import viewsets,generics
from rest_framework.filters import SearchFilter
from django.db import models

from .models import Book, Author, Genre
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()  # ← ТУТ было неправильно
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # поиск
    filter_backends = [SearchFilter]
    search_fields = [
        'title',
        'author__name',
        'genre__name',
    ]
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

