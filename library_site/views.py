from django.shortcuts import render, get_object_or_404
from library_api.models import Book, Author

def index(request):
    return render(request, "index.html")

def books(request):
    return render(request, "books.html", {"books": Book.objects.all()})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_detail.html", {"book": book})

def authors(request):
    return render(request, "authors.html", {"authors": Author.objects.all()})
