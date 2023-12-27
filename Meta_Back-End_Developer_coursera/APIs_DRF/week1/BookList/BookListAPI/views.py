from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import Http404
import json

from .models import Book
from .serializers import BookSerializer


@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title=title, 
            author=author, 
            price=price
        )
        
        try:
            book.save()
        except IntegrityError:
            return JsonResponse(
                {'error': 'true', 'message': 'required field missing'}, 
                status=400
            )
            
        return JsonResponse(model_to_dict(book), status=201)


@csrf_exempt
def books_id(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=204)
    