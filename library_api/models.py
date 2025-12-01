from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)  # например, описание
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    year = models.IntegerField()
    image = models.URLField(blank=True)
    audio_file = models.FileField(upload_to='audio_books/', blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
