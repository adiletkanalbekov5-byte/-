from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books),
    path('books/<int:pk>/', views.book_detail),
    path('authors/', views.authors),
    path('authors/<int:pk>/', views.genre_detail),
    path('genres/', views.genres),
    path('genres/<int:pk>/', views.genre_detail),
]
