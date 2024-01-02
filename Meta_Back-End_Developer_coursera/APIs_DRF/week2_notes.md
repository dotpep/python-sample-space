DRF - django rest framework for APIs development.

- Easy to integrate
- Web browsable API
- Request and response processing objects
- Human readable HTTP Status code 
- CRUD helpers
- Serializers and Deserialization - data conversion, conversion of non-ORM objects, model data to json, json to model data.
- authentication and 


DRF utility app:
![[Pasted image 20231229033023.png|600]]

---
Serialization (transforming or converting database model data to JSON for RESTful API like `pydantic` or `json.loads, json.dumps):
![[Pasted image 20231229033112.png|500]]
![[Pasted image 20231229033901.png|500]]
Deserialization: 
![[Pasted image 20231229033940.png|500]]

---
Authentication system (authorize with external social connection like Google, Facebook and etc.)


---

### Setting up DRF

- `mkdir BookList`
- `cd .\BookList\`
- `pip install pipenv`
- `pipenv install django`
- `pipenv install djangorestframework`
- `pipenv shell`
- `django-admin startproject BookList .`
- `python manage.py startapp BookListAPI`
- `activate .\BookList`
- `django manage.py migrate`
- `cd .\BookListAPI\`
- `touch urls.py` or `code urls.py` (if code then vs code, save file by ctrl+s and continue) in app-level.
- change settings.py `INSTALLED_APPS = ['rest_framework', 'BookListAPI']` and urls.py in project-level `from django.urls import include urlpatterns = [ path('api/', include('BookListAPI.urls'))]`
- implement: models, views, urls.py `from . import views urlpatterns = [ path('books/', views.books) ]` in app-level.
- `django manage.py runserver`

---
settings.py
```python
INSTALLED_APPS = [
	...
    'rest_framework',
    'BookListV2API',
]
```

---
urls.py (project-level)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BookListV2API.urls')),
]
```

---
urls.py (app-level)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books)
]
```

---
views.py
```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view()
def books(request):
    return Response('list of the book', status=status.HTTP_200_OK)
```

---
you can also add database ORM:

models.py
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
```

---
serializers.py (app-level)
```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']
        #fields = '__all__' 
```

---
admin.py
```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

---
views.py 
```python
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def books(request):
    # Get all books
    books = Book.objects.all()
    # Serialize the data
    serializer = BookSerializer(books, many=True)
    # Return the response
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def book(request, pk=None):
    if request.method == 'GET':
        # Get a specific book by id
        book = get_object_or_404(Book, pk=pk)
        # Serialize the data
        serializer = BookSerializer(book)
        # Return the response
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Create a new book
        serializer = BookSerializer(data=request.data)
        # Validate the data
        if serializer.is_valid():
            # Save the data
            serializer.save()
            # Return the response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        # Update a book partially
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        # Validate the data
        if serializer.is_valid():
            # Save the data
            serializer.save()
            # Return the response
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Delete a book
        book = get_object_or_404(Book, pk=pk)
        # Delete the object
        book.delete()
        # Return the response
        return Response(status=status.HTTP_204_NO_CONTENT)
```

---
urls.py (app-level)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books - get all books'),
    path('books/<int:pk>/', views.book, name='book - get, post, patch, or delete a book by id'),
]
```

---

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

---
Django Shell

- `python manage.py shell`
```powershell
>>> from BookListAPI.models import Book
>>> obj = Book(title="book name 1", author="author 1", price=2.55)
>>> obj.save()
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
>>> obj = Book(title="title 2", author="author 2", price=9.99)     
>>> obj.save
<bound method Model.save of <Book: Book object (None)>>
>>> obj.save()
>>> Book.objects.get(pk=2) 
<Book: Book object (2)>
>>> exit()
```

---
Dunder method (string output)

models.py
```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
```

- `python manage.py shell`
```powershell
>>> from BookListAPI.models import Book
>>> obj = Book(title="tt3", author="aa3", price=10.85)       
>>> obj.save()
>>> Book.objects.all()
<QuerySet [<Book: book name 1>, <Book: title 2>, <Book: tt3>]>
>>> Book.objects.get(pk=3) 
<Book: tt3>
>>>
>>> books = Book.objects.all() 
>>> books
<QuerySet [<Book: book name 1>, <Book: title 2>, <Book: tt3>]>
>>> books.update(title='new title', author='new author', price=0.00)
3
>>> books
<QuerySet [<Book: new title>, <Book: new title>, <Book: new title>]>
```

Insert new values into Book model:
```powershell
>>> new_values = [
...     (1, 'mark aurelius', 'meditations', 5.99),
...     (2, 'Lao Tzu', 'Tao Te Ching', 12.99),
...     (3, 'robert martin', 'clean code', 39.99)
... ]
>>> for book, values in zip(Book.objects.all(), new_values):
...     book.pk = values[0]
...     book.author = values[1]
...     book.title = values[2]
...     book.price = values[3]
...     book.save()
... 
>>> books = Book.objects.all()
>>> books
<QuerySet [<Book: meditations>, <Book: Tao Te Ching>, <Book: clean code>]>
```

Capitalize title and author field values:
```python
>>> # Get all the books    
>>> books = Book.objects.all()
>>> # Iterate over the books
>>> for book in books:
...     # Capitalize the title and author fields
...     book.title = book.title.title()
...     book.author = book.author.title()
...     # Save the book object with the updated fields
...     book.save(update_fields=['title', 'author'])
...
>>> books
<QuerySet [<Book: Meditations>, <Book: Tao Te Ching>, <Book: Clean Code>]>
```

---
```python
def update_book_values_by_fields(primary_key, fields, new_value):
    # Get the book object by its primary key
    book = Book.objects.get(pk=primary_key)
    # Get the field names of the book model
    field_names = [field.name for field in Book._meta.get_fields()]
    # Iterate over the fields parameter, which should be a list or a tuple of field names
    for field in fields:
        # Check if the field name is valid
        if field in field_names:
            # Set the new value for the field
            setattr(book, field, new_value)
    # Save the book object with the updated fields
    book.save(update_fields=fields)
```

```powershell
book = Book.objects.get(pk=primary_key) # get the book object by its primary key
book.title = 'new title' # assign the new value for the title field
book.price = 9.99 # assign the new value for the price field
book.save(update_fields=['title', 'price']) # save the object with the updated fields
```

### Different types of routing in DRF

**Regular routes (@api_view)**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),
]
```
```python
from rest_framework.decorators import api_view
@api_view([‘GET’,’POST’])
def books(request):
	...
```

---
**Routing to a class method (class method @api_view)**
```python
class Orders():
    @staticmethod
    @api_view()
    def listOrders(request):
        return Response({'message':'list of orders'}, 200)
```
```python
from django.urls import path
from . import views
urlpatterns = [
    path('orders', views.Orders.listOrders)
]
```

---
**Routing class-based views (using APIView)**
```python
class BookView(APIView):
    def get(self, request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
```
```python
from django.urls import path
from . import views
urlpatterns = [
    path('books/<int:pk>',views.BookView.as_view())
]
```

---
**Routing classes that extend viewsets (using ViewSets)**
```python
Class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message":"All books"}, status.HTTP_200_OK)
    def create(self, request):
        return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
```
```python
urlpatterns = [
    path('books', views.BookView.as_view(
        {
            'get': 'list',
            'post': 'create',
        })
    ),
    path('books/<int:pk>',views.BookView.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        })
    )
]
```

---
**Routing with SimpleRouter class in DRF**
```python
from rest_framework.routers import SimpleRouter
router = SimpleRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```
After mapping, you can access the `api/books` and `api/books/1` endpoints with the same methods as in the previous example.

---
**Routing with DefaultRouter class in DRF**
```python
from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```
Again, after mapping, you can access the `api/books` and `api/books/1` endpoints with the same methods as in the previous examples.
Additionally, you can access the API root view when you visit the `http://127.0.0.1:8000/api/` endpoint. This will display all the available endpoints as in the screenshot below.

![[Pasted image 20231230223636.png|500]]

### Function and Class-based views

##### Class based GET and POST method 

Class based GET and POST method 
- Get list of books
- Create new book
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request):
        return Response({"message": "list of the books"}, status=status.HTTP_200_OK)
        
    def post(self, request):
        return Response({"message": "new book created"}, status=status.HTTP_201_CREATED)
```
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookList.as_view(), name='class based view for GET all books, POST create book')
]
```

---
Class based views by QueryString endpoints:
- `/api/books?author=Adrian` return: `HTTP 200 OK "message": "list of the books by Adrian"` - `GET /api/books?author=Name`
```python
class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message": "list of the books by" + author}, status=status.HTTP_200_OK)
```

---
Payload JSON data for POST requests (return title of payload):
- `{"title": "Seawolf", "author": "Wolfstreet"}` return: `HTTP 201 Created "title": "Seawolf"` - `POST /api/books`
```python
class BookList(APIView):
    def post(self, request):
        return Response({"title": request.data.get('title')}, status=status.HTTP_201_CREATED)
```

---
##### Class based GET and POST method 
Class based GET and PUT method for Get specific book by id/pk
- Get one single specific id/pk book
- Put or Update one single book data
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Book(APIView):
        def get(self, request, pk):
            return Response({"message": "single book with id " + str(pk)}, status=status.HTTP_200_OK)

        def put(self, request, pk):
            return Response({"title": request.data.get('title')}, status=status.HTTP_200_OK)
```
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:pk>', views.Book.as_view(), name='GET specific book, '),
]
```

### Django Debug Toolbar

- `pipenv shell`
- `pipenv install django-debug-toolbar`

settings.py
```python
INSTALLED_APPS = [
    'debug_toolbar',
]
```
urls.py (project level)
```python
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
]
```
settings.py
```python
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```
```python
INTERNAL_IPS = [
    '127.0.0.1'
]
```

---
![[Pasted image 20240102005548.png|700]]

### Serializers

Serializers make Data Conversion (Django ORM model Python to JSON, txt) like Pydantic 

![[Pasted image 20240102032748.png|600]]
![[Pasted image 20240102032815.png|600]]

---

Serialization
![[Pasted image 20240102032848.png|600]]

Deserialization
![[Pasted image 20240102032933.png|600]]

---

##### Serializers example

models.py
```python
from django.db import models

class MenuItem(models.Model):
    """Model definition for MenuItem."""
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        """Unicode representation of MenuItem."""
        return self.title
```

---
views.py
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import MenuItem
from .serializers import MenuItemSerializer


@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request, id):
    #item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)
```
- `get_object_or_404` returns if pk/id is not found in db: `GET /api/menu-items/4444 HTTP 404 Not Found "detail": "Not found."` 

urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:pk>', views.single_item),
]
```
admin.py
```python
from django.contrib import admin
from .models import MenuItem

admin.site.register(MenuItem)
```

---
Serializers example:
serializers.py
```python
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory = serializers.IntegerField()
```

---
Model Serializers example: 
serializers.py only for title and price fields
```python
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price']
```
serializers.py for all of fields
```python
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
```

---
serializers.py modified field (changing data)
```python
from rest_framework import serializers
from .models import MenuItem

from decimal import Decimal

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'stock', 'price_after_tax']

    def calculate_tax(self, product: MenuItem) -> float:
        return round(product.price * Decimal(1.1), 2)
```

---
Relationship Serializers

models.py
```python
from django.db import models

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        """Unicode representation of MenuItem."""
        return self.title
```
- make migrations and migrate

serializers.py
```python
from rest_framework import serializers
from .models import MenuItem
from .models import Category

from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem) -> float:
        return round(product.price * Decimal(1.1), 2)
```

---
min and max value in serializers.py fields
- `stock = serializers.IntegerField(source='inventory', required=False, min_value=0)`
- `extra_kwargs = {'price': {'min_value': 2}, #'stock': {'min_value': 0}}`
```python
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory', required=False, min_value=0)
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)  # method 1 to show Nested fields
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']

        extra_kwargs = {
            'price': {'min_value': 2},
            #'stock': {'min_value': 0}
        }
```

### Deserialization and validation

views.py
```python
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        #serialized_item = MenuItemSerializer(items, many=True)
        serialized_item = MenuItemSerializer(items, many=True, context={'request': request})  # for hyperlink
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        #serialized_item.validated_data
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, pk):
    #item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem, pk=pk)  # show 404 error if there is no pk=id
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)
  
# Display a related model fields field as a hyperlink
@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)
```

serializers.py
- `category = CategorySerializer(read_only=True)`
- `category_id = serializers.IntegerField(write_only=True)`
```python
from rest_framework import serializers
from .models import MenuItem
from .models import Category

from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    #category = serializers.StringRelatedField()  # show title of Category model using dunder str method
    category = CategorySerializer(read_only=True)  # method 1 to show Nested fields
    #category = serializers.HyperlinkedRelatedField(queryset = Category.objects.all(), view_name='category-detail')  # category as hyperlink
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        #depth = 1  # method 2 to show Nested fields

    def calculate_tax(self, product: MenuItem) -> float:
        return round(product.price * Decimal(1.1), 2)
```

### Renderers

- [Renderers - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/renderers/)

settings.py
```python
# add default DRF renderers
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ]
}
```

- `pipenv shell`
- `pipenv install djangorestframework-xml`

---
Django REST Framework XML Renderers:
```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        ...
        'rest_framework_xml.renderers.XMLRenderer',
    ]
}
```

- `http://127.0.0.1:8000/api/menu-items?format=xml`
![[Pasted image 20240102163533.png|500]]

Insomnia
![[Pasted image 20240102163409.png|500]]

---
Django Rest Framework XML Renderers errors of Using uncorrected virtual environment 
- select interpreter `~/.virtualenvs/LittleLemon-2bmZWwXa` in vs code
- open new powershell terminal in vs code
- `activate ./LittleLemon` if  needed
- `pip list` check with `pipfile` created by pipenv.
```powershell
>>> PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF> & C:/Users/pepel/.virtualenvs/LittleLemon-2bmZWwXa/Scripts/Activate.ps1
>>> (LittleLemon) PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF> cd .\week2\LittleLemon\
>>> (LittleLemon) PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF\week2\LittleLemon> deactivate
>>> PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF\week2\LittleLemon> & C:/Users/pepel/.virtualenvs/LittleLemon-2bmZWwXa/Scripts/Activate.ps1
>>> (LittleLemon) PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF\week2\LittleLemon> pipenv shell

Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv tWindows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

Wellcome dotpep GoodLuck in your Development Journey.

>>> PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF\week2\LittleLemon> pipenv install djangorestframework-xml
Installing djangorestframework-xml...
Resolving djangorestframework-xml...
Installation Succeeded
Installing dependencies from Pipfile.lock (688a50)...
>>> PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF\week2\LittleLemon> pipenv requirements       
asgiref==3.7.2; python_version >= '3.7'
defusedxml==0.7.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
django==5.0.1; python_version >= '3.10'
djangorestframework==3.14.0; python_version >= '3.6'
djangorestframework-xml==2.0.0; python_version >= '3.5'
pytz==2023.3.post1
sqlparse==0.4.4; python_version >= '3.5'
typing-extensions==4.9.0; python_version < '3.11'
tzdata==2023.4; sys_platform == 'win32'
>>> PS D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF\week2\LittleLemon> pip list
Package                 Version
----------------------- ------------
asgiref                 3.7.2
defusedxml              0.7.1
Django                  5.0.1
djangorestframework     3.14.0
djangorestframework-xml 2.0.0
pip                     23.3.2
pytz                    2023.3.post1
setuptools              69.0.3
sqlparse                0.4.4
typing_extensions       4.9.0
tzdata                  2023.4
wheel                   0.42.0
```


### SRC

- class vs functional views in django
- indexes and serialization in Django Model
- api_view, api_view and staticmethod, APIView, viewsets.ViewSet - what's difference in DRF
- Response and JsonResponse - difference between in DRF
- path, as_view, include and SimpleRouter, DefaultRouter in Django URLs routing
- QuerySet and Django shell, Django model
- Generic views and ViewSets in DRF
- Query String in DRF api endpoint development
- django function vs class based views
- drf apiview vs generics api view
- [Serializer fields - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/fields/)
- [QuerySet API reference | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/5.0/ref/models/querysets/)
- [Home - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/)
- [Django Debug Toolbar — Django Debug Toolbar 4.2.0 documentation (django-debug-toolbar.readthedocs.io)](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [Routers - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/routers/)

---

- django orm objects.select_related()
- drf nested serializer and relationship model serialization
- django model serializers hyperlink JSON
- drf serializer
- drf deserialization and validation
- drf renderers
- [Renderers - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/renderers/)
- [mjumbewu/django-rest-framework-csv: CSV Tools for Django REST Framework (github.com)](https://github.com/mjumbewu/django-rest-framework-csv)
- [djangorestframework-xml (jpadilla.github.io)](https://jpadilla.github.io/django-rest-framework-xml/)
- [djangorestframework-yaml (jpadilla.github.io)](https://jpadilla.github.io/django-rest-framework-yaml/)
- [djangorestframework-jsonp (jpadilla.github.io)](https://jpadilla.github.io/django-rest-framework-jsonp/)