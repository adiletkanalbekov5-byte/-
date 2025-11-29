from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/', blank=True, null=True)  # <- это поле добавляем
    bio = models.TextField(blank=True, null=True)  # например, описание
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    year = models.IntegerField()
    image = models.URLField(blank=True)

    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
