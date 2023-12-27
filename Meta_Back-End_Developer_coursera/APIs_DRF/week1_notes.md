API - Application programming interface
APIs - is gateway to access back-end application and data.

Key moment of this course:
- http
- REST APIs
- authentication and authorization
- DRF
- serialization and deserialization
- API endpoints (or URL paths)
- render API output as JSON and XML data
- throttling and caching to optimize and protect your API
- caching to save API infrastructure resources
- token-based authentication
- search, ordering, filtering and pagination

---
### Intro to APIs

#### HTTP/HTTPS
HTTP - Hyper text transport protocol (application layer in TCP/IP и OSI models that works on top of TCP, or just use this.)

HTTP request and response
Client <-> data <-> Server

HTTPS - secure of HTTP that using TLS/SSL encryption, and based upon transmission of TLS/SSL certificates, which verify that a particular provider is who they say they are.
![[Pasted image 20231218181339.png]]

---
#### HTTP methods 

just CRUD operation:
- GET
- POST
- PUT
- PATH
- DELETE
![[Pasted image 20231218181536.png|600]]

|**HTTP method**|**Action**|
|---|---|
|GET|Returns the requested resource. If not found, returns a 404 Not Found status code.|
|POST|Creates a record. The POST request always comes with an HTTP request body containing JSON or Form URL encoded data, which is also called a payload. If the data is valid, the API endpoint will create a new resource based on these data. Although you can create multiple resources with a single POST call, it is not considered a best practice to do so.|
|PUT|Instructs the API to replace a resource. Like a POST request, the PUT request also comes with data. A PUT request usually supplies all data for a particular resource so that the API developer can fully replace that resource with the provided data. A PUT request deals with a single resource.|
|PATCH|Tells the API to update a part of the resource. Note the difference between a PUT and a PATCH call. A PUT call replaces the complete resource, while the PATCH call only updates some parts. A PATCH request also deals with a single record.|
|DELETE|Instructs the API to delete a resource.|

---
Example of calls HTTP methods:

|**HTTP method**|**Sample endpoints**|**Query string / payload**|
|---|---|---|
|GET|/api/menu-items<br><br>/api/meu-items/1<br><br>/api/menu-items?category=appetizers<br><br>/api/menu-items?perpage=3&page=2|A GET call doesn’t need a payload. However, GET calls can be accompanied by query string parameters and their values to filter the API output.|
|POST|/api/menu-items<br><br>/api/orders|Here’s a sample JSON payload for the /api/menu-items endpoint to create a new resource:<br><br>{<br><br>  "title":"Beef Steak",<br><br>  "price": 5.50,<br><br>  "category":"main",<br><br>}|
|PUT|/api/menu-items/1<br><br>/api/orders/1|Here's a sample JSON payload for this endpoint /api/menu-items/1 to completely replace it. Note that you need to supply all data for a PUT request.<br><br>{<br><br>  "title":"Chicken Steak",<br><br>  "price": 2.50,<br><br>  "category":"main",<br><br>}|
|PATCH|/api/menu-items/1<br><br>/api/orders/1|Here’s a sample JSON payload for this endpoint /api/menu-items/1 to partially update this resource<br><br>{<br><br>   "price": 3.00<br><br>}|
|DELETE|/api/menu-items<br><br>/api/menu-items/1<br><br>/api/orders<br><br>/api/orders/1|When the DELETE call is sent to a collection endpoint, like /api/menu-items the API developer should delete the entire collection. When it is sent to a particular resource, like this, /api/menu-items/1, then the API developer should delete only that resource.|

---
HTTP request - different types of information encoded by a browser.

- Version type (2/)
- URL
- Method
- Request header - HTTP request header, extra information for server (Cookies, User-agents, Referrers)
- Request body - HTTP body, input data

- HTTP response, information that helps browser display content (requested resource, content length, content type, headers, etags, time last modified, HTTP status code)

---
#### Response types

|**Response type**|**Request header**|
|---|---|
|HTML|Accept: text/html|
|JSON and JSONP|Accept: application/json|
|XML|Accept: application/xml<br><br>Accept: text/xml|
|YAML|Accept: application/yaml<br><br>Accept: application/x-yaml<br><br>Accept: text/yaml|

#### HTTP status code

![[Pasted image 20231218182201.png|400]]

![[Pasted image 20231218182245.png|700]]

---

|**Status code range**|**Purpose**|
|---|---|
|100-199|This range is mainly used to pass on some information. For example, sometimes an API needs time to process the request and it can’t instantly deliver the result. In such a case, the API developer can set it to keep returning 102 – Processing until the result is ready. This way, the client understands that the result isn’t ready and should be checked again.|
|200-299|These are the success codes. If the client requests something and the API acts successfully, it should deliver the output with one of these status codes.  <br><br>For example, for a  PUT, PATCH, or DELETE call, you can return 200 – Successful if the operation was successful. For a successful POST call, you can set it to return a 201 – Created status code when the resource has been created successfully.|
|300-399|These are the redirection codes. Suppose as an API developer, you changed the API endpoint from /api/items to api/menu-items. If the client makes an API call to /api/items, then you can redirect the client to this new endpoint /api/menu-items with a 301 – Permanently moved status code so that the client can make new calls to that endpoint next time.|
|400-499|4xx status codes are used in the following situation: if the client requests something that does not exist, sends an invalid payload with insufficient data, or wants to perform an action that the client is not authorized for.<br><br>For the above scenarios, the appropriate status codes will be:<br><br>·       404 - Not Found if the client requests something that doesn’t exist,<br><br>·       400 - Bad Request if a client sends an invalid payload with insufficient data,<br><br>·       401 - Unauthorized,<br><br>·       403 - Forbidden if the client tries to perform an action it's not authorized for.|
|500-599|These alarming status codes are usually automatically generated on the server side if something goes wrong in the code, and the API developer doesn't write code to deal with those errors. For example, a client requests a non-existing resource, and the API developer tries to display that resource without adequately checking if that resource exists in the database. Or if the API developer didn't validate the incoming data and attempted to create a new resource with invalid or insufficient data. You, as an API developer, should always avoid 5xx errors.|

#### RESTfulness

API - Application programming interface. Gateway to back-end data (access and modify).

REST is an architectural style for designing APIs for your project.
- easy and quick dev
![[Pasted image 20231218183757.png|500]]

RESTful - constraints
- Client-server (architecture)
- Stateless (no prier info included)
- Cacheable (responses can be saved)
- Layered (system can be split into layers)
- Uniform interface (unique URLs, unified procedures, XML or JSON)
- Optional, code on demand (business logic)

![[Pasted image 20231218184158.png|700]]

Resources - core part of every REST API
![[Pasted image 20231218184532.png|700]]

---
**Resource type:**
manager use APIs:
![[Pasted image 20231218184641.png|700]]
![[Pasted image 20231218184807.png|700]]
![[Pasted image 20231218184830.png|700]]
![[Pasted image 20231218184850.png|700]]

---
customer use APIs
![[Pasted image 20231218184949.png|700]]

---
customer unpack
![[Pasted image 20231218185059.png|700]]

---
Stateless:
![[Pasted image 20231218185204.png|700]]
instead uses this URLs/endpoints
![[Pasted image 20231218185330.png|700]]

#### Naming conventions

![[Pasted image 20231218194537.png|700]]

must be:
> [!success] correct usage
> - lowercase letter
> - hyphens in between words 
> - meaning name
> - forward slash for object - hierarchical relationships between related objects

avoid this:
> [!failure] wrong
> - snake_case
> - TitleCase
> - camelCase



---
![[Pasted image 20231218194840.png|500]]
![[Pasted image 20231218194859.png|500]]
![[Pasted image 20231218194912.png|500]]

---
**==Use forward slashes for hierarchy==**

![[Pasted image 20231218195049.png|400]]
![[Pasted image 20231218195118.png|500]]
![[Pasted image 20231218195155.png|500]]

![[Pasted image 20231218195219.png]]

> [!success] correct usage
> - `https://little.lemon/orders/{orderId}/customer-details`

---
**==Nouns==** 

![[Pasted image 20231218195328.png|500]]

bad naming, wrong (never with verbs):
> [!failure] wrong
> - `/getAllBooks`
> - `/getUser/{userId}`
> - `/users/{userId}/delete` uses delete HTTP methods in naming
> - `/orders/{orderId}/save`


![[Pasted image 20231218195615.png|500]]

REST APIs returns json or xml
wrong naming:
> [!failure] wrong
> - `orders/{orderId}.json`
> - `orders/{orderId}.xml`

> [!success] correct usage
> - `orders/{orderId}?format=json`
> - `orders/{orderId}?format=xml`
> Minified version of a JavaScript file
> - `/asserts/js/jquery/3.6.0/min`
> - `/asserts/js/moment/2.29.4/original`

---
**Query string parameter**

![[Pasted image 20231218200946.png|500]]
![[Pasted image 20231218201030.png|500]]

---
No trailing slash (in end of endpoints)

> [!failure] wrong
> `/orders/{orderId}/`
> ends with slash /

> [!success] correct usage
> `/orders/{orderId}`
> `/sports/basketball/teams`
> without slash in ends of endpoint

#### Good routes versus bad routes (endpoints, URLs path)

Naming your API properly is the first step in designing a good API. When the API name follows a convention, it provides lots of information about the API and its purpose. To create a meaningful API endpoint, you need to follow some simple guidelines and rules.

##### Rule 01: Everything in lowercase, with hyphens and not abridged

The URI of your API should always be in lowercase. Do not use camelCase, PascalCase or Title case when you design your API. Also, separate multiple words using hyphens, not underscores. Do not keep abridged, or shortened, words in your URI; always use the full and meaningful form.

If your API accepts a variable, you should always represent it in camelCase, and wrap it inside a set of curly braces {}.

|**URI**|**Status**|**Why**|
|---|---|---|
|/customers|Good|Plural and lowercase|
|/customers/16/phone-number|Good|Lowercase and hyphen used to separate words|
|/customers/16/address/home|Good|Lowercase, no trailing slash, displays the hierarchical relationship with forward slashes.|
|/users/{userId}|Good|Variable in camelCase, and no hyphen in the variable name|
|/Customers|Bad|Title case|
|/generalMembers|Bad|camelCase, no hyphens to separate words|
|/MenuItems<br><br>/GeneralMembers|Bad|Pascal case|
|/customers/16/tel-no|Bad|Abbreviation|
|/customers/16/phone_number|Bad|Underscores|
|/customers/16/phonenumber|Bad|No separation of words|
|/users/{user-id}|Bad|Variable should be in camelCase, and hyphen between words|

##### Rule 02: Use a forward slash to indicate a hierarchical relationship

In your API URI, always use the forward slash to indicate a hierarchical relationship. To understand this rule, consider the following scenarios and the relationship from the API endpoints.

A store can have customers who have placed many orders and each of these orders can have delivery addresses, menu items and bills.

|**URI**|**Status**|
|---|---|
|/store/customers/{customerId}/orders|Good|
|/store/orders/{orderId}|Good|
|/store/orders/{orderId}/menu-items|Good|

Similarly, a library can have books from many authors. Each of these books has an ISBN number.

|**URI**|**Status**|
|---|---|
|/library/authors/books|Good|
|/library/book/{bookId}/isbn|Good|

##### Rule 03: Use nouns for resource names, not verbs

One of the most prominent features of REST APIs is that it uses nouns to indicate resources, not verbs. And you should always stick to this rule when designing your API. You should also use plural nouns to indicate a collection.

|**URI**|**Expects**|**Status**|**Why**|
|---|---|---|---|
|/orders|Collection|Good|Uses a noun, not a verb|
|/users/{userId}|Single user|Good|Uses a noun and proper hierarchical relationship and naming convention|
|/order|Collection|Bad|Uses plural nouns for collections|
|/getOrder|Single resource|Bad|Uses a verb, camelCase|
|/getUser/{userId}|Single user|Bad|Uses a verb, camelCase|

##### Rule 04: Avoid special characters

You should always avoid special characters in your API endpoints. They can be confusing and technically complex for your users. Consider the following bad examples.

|**URI**|**Status**|**Why**|
|---|---|---|
|/users/12\|23\|23/address|Bad|Special character \||
|/orders/16/menu^items|Bad|Special character ^|

If your API can accept multiple user ids, then they should be separated using a comma, as demonstrated below.

|**URI**|**Status**|**Why**|
|---|---|---|
|/users/12,23,23/address|Good|Uses a comma for separation|

##### Rule 05: Avoid file extensions in URI

You should always avoid file extensions in your API names. For example, if your API can deliver an output in both JSON and XML format, it should never look like this.

|**URI**|**Status**|**Why**|
|---|---|---|
|/sports/basketball/teams/{teamId}.json|Bad|File extension at the end|
|/sports/basketball/teams/{teamId}.xml|Bad|File extension at the end|

Instead, your client should be able to indicate its expected format in a query string, just like this.

|**URI**|**Status**|**Why**|
|---|---|---|
|/sports/basketball/teams/{teamId}?format=json|Good|No file extension|
|/sports/basketball/teams/{teamId}?format=xml|Good|No file extension|

Similarly, if your API is serving a static file, for example, CSS or JavaScript files, you should use endpoints like the following to deliver the minified and original source file. You can also use a query string to get the minified or original version. Some API developers use the output format like file extension at the end of the regular API endpoints, which is also bad practice.

|**URI**|**Status**|**Why**|
|---|---|---|
|/assets/js/jquery/3.12/min|Good|No file extension|
|/assets/js/jquery/3.12/source|Good|No file extension|
|/assets/js/jquery/3.12/?format=min|Good|No file extension|
|/assets/js/jquery/3.12/?format=source|Good|No file extension|
|/menu-items?format=json|Good|Perfectly named endpoint with expected output format in a query string|
|/menu-items.json|Bad|Uses the expected output format as the file extension|

##### Rule 06: Use query parameters to filter when necessary

When designing your API, you should always perform data filtering using a query string. This is the same when you expect some extra parameters, like the number of items per page and page number.

Consider this example of a travel site. You want to find which locations a particular user has traveled to. And then you want to know which locations in the USA the user has already seen.

|**URI**|**Status**|**Why**|
|---|---|---|
|/users/{userId}/locations|Good|Hierarchical|
|/users/{userId}/locations?country=USA|Good|camelCase, no separation of words|
|/articles?per-page=10&page=2|Good|Proper use of query string|
|/users/{userId}/locations/USA|Bad|Doesn't use a query string to filter data|
|/articles/page/2/items-per-page/10|Bad|Redundant and obscure|

##### Rule 07: No trailing slash

When sharing your API endpoint with others in your team, or in public, avoid using a trailing slash at the end of your API endpoints. Consider the following examples.

|**URI**|**Status**|**Why**|
|---|---|---|
|/users/{userId}|Good|No trailing slash|
|/articles/{articleId}/author|Good|No trailing slash|
|/users/{userId}/|Bad|Trailing slash|
|/articles/{articleId}/author/|Bad|Trailing slash|

#### Tools for APIs (Insomnia)

**Curl - HTTP calls from command line**
- `curl https://postman-echo.com/get?project=LittleLemon`
- `curl -d "project=LittleLemon" -X POST https://postman-echo.com/post`
 

**Tools for API:**
Postman - test and debug APIs.
Insomnia - store, organize, and execute REST API requests. 


This is free service experiment with different http methods
- `https://httpbin.org/get?project=LittleLemon`

#### Setting up tools and environment

- Install VS Code
- Install Python
- Install VS Code Python extension
- Additional extensions in VS Code (**`Python Indent`** by Kevin Rose to correct Python indentation in VS Code, and **`Djaneiro`** by Scott Barkman for useful Django snippets.)
- Install a package manager - `pip install pipenv`
	pipenv lets you easily create virtual environments for your projects so that you can manage your dependencies more efficiently.
	Like 


#### Setup Django project using pipenv

- `mkdir LittleLemon`
- `cd .\LittleLemon\`
- `pipenv install django`
- `pipenv shell` to activate venv

- `django-admin startproject LittleLemon`
- `cd .\LittleLemon`
- `python .\manage.py startapp LittleLemonAPI`
- `python .\manage.py runserver`
- `python .\manage.py runserver 9000` in specific port

---
**Pipfile** this file contains details of the dependencies for the project. 

1. copy and paste this into `Pipfile`:
```python
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"
djangorestframework = "*"
djangorestframework-xml = "*"
djoser = "*"

[dev-packages]

[requires]
python_version = "3.9"
```

2. Run this command to install dependencies using updated **Pipfile**: `pipenv install`
3. `python3 manage.py startapp LittleLemonDRF`
4. `python3 manage.py runserver`



### Principles of API development

#### REST best practices

you need to spend time with Architecture design of REST this is best practice:
- KISS (Keep It Simple Stupid)
- Filter, order and pagination
- Versioning
- Caching
- Rate limiting
- Monitoring

---
KISS - One specific API do One specific Job
update date using `PUT` or `PATCH` HTTP methods
![[Pasted image 20231218221718.png|500]]

---
Filter, order and paginate - filter large result sets and rearrange them it Ascending or Descending order, using pagination you an deliver results in smaller chunks.
![[Pasted image 20231218222014.png|600]]
but client want to see only `deserts` in menu, you must give filter using query string, to retrieve only `appetizers` or `deserts`, or `mains`
![[Pasted image 20231218222122.png|600]]
pagination with chunks (Page 10 of 16)
![[Pasted image 20231218222347.png|600]]

---
another practice is Versioning
![[Pasted image 20231218222503.png|400]]

---
Caching
![[Pasted image 20231218222546.png|500]]
![[Pasted image 20231218222625.png|500]]

---
Rate limiting
- limits calls

---
Monitoring
- response time
- HTTP status code (range of 400, 500)
- bandwidth

#### Security and authentication in REST API

Web APIs have risks:
![[Pasted image 20231219023546.png|500]]

---
**SSL - Secure Socket Layer (encrypt) certificate properties give HTTPS.**
![[Pasted image 20231219033102.png|400]]

---
**Signed URLs - limited access to a resource for a limited time.** 

HMAC
![[Pasted image 20231219033243.png|500]]

---
**Authentication** (signed URLs)

> password based authentication
![[Pasted image 20231219033419.png|500]]

> Token based authentication
> HTTP basic authentication

---
CORS (Cross-Origin Resource Sharing) - CORS policy and firewalls. 
![[Pasted image 20231219033945.png|500]]

---
> Firewall application on your server

#### Access control (Role, Privilege, Authentication vs Autorization)

![[Pasted image 20231219034338.png|600]]
![[Pasted image 20231219034508.png|600]]

multiple privilege's:
![[Pasted image 20231219034804.png|600]]

---
**Authentication:**
![[Pasted image 20231219035405.png]]

**Authorization**
![[Pasted image 20231219035549.png]]

---
**Implementing authorization**

For example, for a bookshop, there might be the following types of privileges:
- Browse the books
- Add new books
- Edit books
- Delete books
- Place orders

![[Pasted image 20231219035918.png]]


### Writing first API (DRF)

Booklist APIs Project (CRUD) planning:
- define Features of project
- creating Django Model for save data ORM - database
- define and create a Endpoint or URI of APIs (`api/books`, `api/books/{book_id}`, this is a URL pattern `api/books/<int:pk>`)
- get Different Response like JSON, Encoded URL
- convert Model to JSON response
- apple Edit, Delete requests
- parse HTTP body to access data element using `QueryDict` class
- write Documentation for APIs using Insomnia or httpbin

#### Booklist APIs Project planning

Django Model:
![[Pasted image 20231225001001.png|700]]

---
API Endpoints:
![[Pasted image 20231225001056.png|700]]
with Status code
![[Pasted image 20231225001205.png|600]]

---
Convert model instance to a JSON response:
![[Pasted image 20231225001310.png|700]]

---
CRUD operation for APIs:
![[Pasted image 20231225001359.png|400]]

URL pattern:
![[Pasted image 20231225001410.png|400]]

---
JSON string:
![[Pasted image 20231225001455.png|500]]

QuertDict:
![[Pasted image 20231225001524.png|500]]


#### Organizing an API project

Splitting project into multiple apps is well practice in programming, decompensate, and modular structure of your project.
Each app must have one specific aims, goals.

Some Terms:
- best practice
- PEP8
- task decomposition
- modular structure
- using some Paradigms like OOP or Functional and mix it as needed, Manager Main Function, Encapsulate functions in modular structure, use `if __name__ == "__main__"` and `__init__.py`
- Clean Code, Architecture design, Blueprint

---
1. split app
2. use virtual env.
3. versioning
4. list dependencies
5. separate resource folder
6. multiple settings files
7. business logic in models or better in services.py

---
1. Use virtual environment and manage dependencies with `pip`, `pipenv`, `env`, `venv`, `poetry` instead global environment  
2. Upgrades might break up
	- use versioning `api/v1/books` and `api/v2/books`
	- and keeping old API intact
	- timely launch
	- save requirements and dependencies of project `pipenv freeze` - list of packages and version this packages that you use in project `pip3 freeze > requirements.txt`
3. Separate resources folder for each app 
	- avoid conflicts and manage files
	- static file
	- split settings (Django split settings)
4. Place for business logic in models or files named `services.py` not in views, templates and etc. specific created django file.py.

---
- API design
- [Consequences of a poorly designed API project | Coursera](https://www.coursera.org/learn/apis/supplement/KqDmX/consequences-of-a-poorly-designed-api-project)
- authentication or authorization and permission
- ssl
- naming conventions API endpoints
- data validation and sanitization
- business logic 
- caching API
- pagination and filtering
- Not following the proper naming convention, not sending proper HTTP codes, not accepting Accept headers, absence of pagination, sorting, searching and filtering, and lack of proper error checking in code.
- Not following the proper versioning system
- Keeping everything in one big Django app, adding all business logic in the views.
- api best practice

### Lab-Project Booklist API

- `pip install django`
- `django-admin startproject BookList`
- `cd BookList`

Create virtual environment for project:
```shell
pipenv shell
```
- `pipenv install django`
- update Pipfile packages file and install this dependencies:  `pipenv install`
- `pipenv install django`
- `python manage.py startapp BookListAPI`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

- `python manage.py shell`

---
settings.py
```python
INSTALLED_APPS = [
    'rest_framework',
    'BookListAPI',
]
```
project-level, urls.py
```python
from django.contrib import admin
from django.urls import path, include

from BookListAPI import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("BookListAPI.urls")),
]
```
app-level, urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name="all books"),
    path('books/<int:book_id>/', views.books_id, name="specific books with id"),

]
```
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
admin.py
```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```
app-level, serializers.py
```python
from rest_framework import serializers
from .models import Book
  
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']  # __all__
```
views.py
```python
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
        title = data.get('title')
        author = data.get('author')
        price = data.get('price')
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
```

---
![[Pasted image 20231226233051.png]]
![[Pasted image 20231226233120.png]]
![[Pasted image 20231226233137.png]]
![[Pasted image 20231226233153.png]]
![[Pasted image 20231226233211.png]]


### Work with Debug tools in VS code for django project 

- debug > choose JSON > python > django

views.py
```python
numbers = [x for x in range(1, 7)]

def display_even_numbers(request):
    response = ""
    for i in numbers:
        remainder = i % 2
        if remainder == 0:
            response += str(i) + "<br/>"
    return HttpResponse(response)

def display_odd_numbers(request):
    response = ""
    for i in numbers:
        if i % 2 == 1:
            response += str(i) + "<br/>"
    return HttpResponse(response)
```
urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('even/', views.display_even_numbers),
    path('odd/', views.display_odd_numbers),
]
```

- set endpoints for line of code 
- add to watch a variable (like `reminder`) that you want monitor
- start (F5) 
- `http://127.0.0.1:8000/numbers/` enter this URLs or Refresh page (this starts your django debug tools)
- step into (F10)
- restart debug (CTRL + SHIFT + F5)

### Browser tools for API development and back-end

for API - use Fetch/XHR filters:
![[Pasted image 20231227000317.png]]


---
![[Pasted image 20231227003626.png|500]]
![[Pasted image 20231227135631.png|500]]

### SRC

- python virtualenv
- pipenv vs poetry
- [Pipenv: Python Dev Workflow for Humans — pipenv 2023.11.16.dev0 documentation (pypa.io)](https://pipenv.pypa.io/en/latest/)
- [Poetry - Python dependency management and packaging made easy (python-poetry.org)](https://python-poetry.org/)
- http in depth
- api
- rest vs restful
- naming api endpoints
- insomnia rest api
- postman
- restful api stateless
- restfulness constraints

- stateless vs stateful programming
- ssl certificate for rest api
- signed urls HMAC
- URI vs URL vs Endpoint
- authentication api
- jwt token
- jwt token django rest framework
- Authentication versus authorization

- [Home - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/)
- [Getting started — djoser 2.2.2 documentation](https://djoser.readthedocs.io/en/latest/getting_started.html)
- [Authentication - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/authentication/)
- [httpbin.org](https://httpbin.org/) 
- [Insomnia Docs](https://docs.insomnia.rest/)
- [Postman API Platform](https://www.postman.com/)
- [Curl command line tool and library for transferring data with URLs](https://curl.se/)


API for Test:
- [public-apis/public-apis: A collective list of free APIs (github.com)](https://github.com/public-apis/public-apis)
- [HTTPie for web and desktop](https://httpie.io/)
- [restcountries.com/v3.1/all](https://restcountries.com/v3.1/all)
- [Postman API platform for building and using APIs](https://www.postman.com/)
- [Postman Echo service to test REST clients and make sample API calls](https://postman-echo.com/)
- [Insomnia homepage](https://insomnia.rest/)
- [Getting started with Insomnia](https://docs.insomnia.rest/insomnia/get-started)
- [Httpbin HTTP request and response service](https://httpbin.org/)  
- [Python homepage](https://python.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python Indent by Kevin Rose](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [Djaneiro by Scott Barkman](https://marketplace.visualstudio.com/items?itemName=thebarkman.vscode-djaneiro)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [Django](https://www.djangoproject.com/)
- [List of HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

- API design
- [Consequences of a poorly designed API project | Coursera](https://www.coursera.org/learn/apis/supplement/KqDmX/consequences-of-a-poorly-designed-api-project)
- authentication or authorization and permission
- ssl
- data validation and sanitization
- business logic 
- caching API
- pagination and filtering
- api best practice

- pydantic vs json
- urllib
- aiohttp vs request
- how to use pipenv
- queryset django
- fetch xhr

---

- [Pipenv: A Guide to the New Python Packaging Tool – Real Python](https://realpython.com/pipenv-guide/#example-usage)
- [Pipenv & Virtual Environments — The Hitchhiker's Guide to Python (python-guide.org)](https://docs.python-guide.org/dev/virtualenvs/)
- [Django: add index to meta field - Stack Overflow](https://stackoverflow.com/questions/33174680/django-add-index-to-meta-field)
- [Pipenv Commands — pipenv 2023.11.16.dev0 documentation (pypa.io)](https://pipenv.pypa.io/en/latest/commands.html#:~:text=Pipenv%20Commands%20%C2%B6%201%20install%20%C2%B6%20%24%20pipenv,%C2%B6%20...%208%20shell%20%C2%B6%20...%20More%20items)
- [Django URLs (w3schools.com)](https://www.w3schools.com/django/django_urls.php)
- [Request and response objects | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/5.0/ref/request-response/)
- [Insomnia Scratch Pad Tutorial | Insomnia Docs](https://docs.insomnia.rest/insomnia/scratchpad#setting-up-request-parameters)
- [Insomnia REST Client Tutorial - YouTube](https://www.youtube.com/watch?v=H16GUC9Svyk)
