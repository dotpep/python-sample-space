# function based views
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

from rest_framework.response import Response
from rest_framework import status

# class based views
from rest_framework.views import APIView

# function based views
@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def book(request, pk=None):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        serializer =BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class based views
class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message": "list of the books by " + author}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "list of the books"}, status=status.HTTP_200_OK)
    
    def post(self, request):
    #    return Response({"message": "new book created"}, status=status.HTTP_201_CREATED)
        return Response({"title": request.data.get('title')}, status=status.HTTP_201_CREATED)


class Book(APIView):
        def get(self, request, pk):
            return Response({"message": "single book with id " + str(pk)}, status=status.HTTP_200_OK)
        
        def put(self, request, pk):
            return Response({"title": request.data.get('title')}, status=status.HTTP_200_OK)
        