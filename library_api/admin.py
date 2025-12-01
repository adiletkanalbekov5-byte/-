from django.contrib import admin
from .models import Book, Author, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", 'image_url')
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year")
    list_filter = ("year", "author")
    search_fields = ("title",)

    def audio_player(self, obj):
        if obj.audio_file:
            return f'<audio controls><source src="{obj.audio_file.url}" type="audio/mpeg"></audio>'
        return "(Нет аудио)"

    audio_player.allow_tags = True
    audio_player.short_description = "Аудио"
