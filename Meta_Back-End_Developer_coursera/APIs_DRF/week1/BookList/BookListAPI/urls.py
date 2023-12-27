from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name="all books"),
    path('books/<int:book_id>/', views.books_id, name="specific books with id"),
]