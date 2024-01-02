from django.urls import path
from . import views

urlpatterns = [
    # function based
    #path('books/', views.books, name='GET all books, create new book using POST'),
    #path('books/<int:pk>/', views.book, name='GET, DELETE and Update using PATCH a book by id or primary key'),
    
    # class based
    path('books', views.BookList.as_view(), name='GET all books, POST create new book'),
    path('books/<int:pk>', views.Book.as_view(), name='GET specific book, '),
]