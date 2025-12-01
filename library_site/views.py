from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from library_api.models import Book, Author, Genre

def books(request):
    search_query = request.GET.get("search", "")
    books = Book.objects.all()

    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__name__icontains=search_query) |
            Q(genre__name__icontains=search_query)
        )

    return render(request, "books.html", {"books": books, "search": search_query})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_detail.html", {"book": book})

def authors(request):
    return render(request, "authors.html", {"authors": Author.objects.all()})

def genres(request):
    return render(request, "genres.html", {"genres": Genre.objects.all()})

def genre_detail(request, pk):
    genre = Genre.objects.get(pk=pk)
    books = Book.objects.filter(genre=genre)
    return render(request, "books.html", {"books": books})

def index(request):
    return render(request, "index.html")

def audio_books(request):
    books_with_audio = Book.objects.filter(audio_file__isnull=False)
    return render(request, "audio_books.html", {"books": books_with_audio})