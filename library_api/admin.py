from django.contrib import admin
from .models import Book, Author, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",'image')
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year")
    list_filter = ("year", "author")
    search_fields = ("title",)
