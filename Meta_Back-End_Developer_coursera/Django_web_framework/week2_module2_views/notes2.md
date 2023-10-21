## View

http request and response


views.py (app level)
```python
from django.http import HttpResponse

# 1

def home(request):

    content = "<html><body><h1>Welcome to little lemon</h1></body></html>"

    return HttpResponse(content)

# 2

def say_hello(request):

    return HttpResponse("Hello World!")
```

urls.py (app level)
```python
from django.urls import path

from . import views # 1

  
urlpatterns = [

    path('', views.home) # 1

]
```

urls.py (project level)
```python
from django.urls import path
from django.urls import include # 1
from demoapp import views # 2

  

urlpatterns = [

    path('admin/', admin.site.urls),
    # 1
    path('', include('demoapp.urls')),
    # 2
    path('say_hello/', views.say_hello),
    ]
```


this is same: 
```python
from . import views
# dot (.) here indicates the same working directory as the file.
from demoapp import views
```


correct URL load (`http://127.0.0.1:8000/little/home`) in this situation
```python
# in project level
urlpatterns = [ path('little/', include('myapp.urls')), ] 
# in app level
urlpatterns = [ path('home/', views.home, name="home"), ]
```


## Requests and URLs

HTTP request:
![[Pasted image 20231020003838.png|500]]
![[Pasted image 20231019235110.png|300]]

---
HTTP methods:
![[Pasted image 20231019235209.png|400]]

---
HTTP response
![[Pasted image 20231019235525.png|400]]

HTTP response Status Codes:
![[Pasted image 20231019235638.png|400]]
![[Pasted image 20231019235808.png|300]]
![[Pasted image 20231019235738.png|300]]

200 OK (status code)
![[Pasted image 20231019235940.png|300]]

---
HTTPS (secure version of http:)
![[Pasted image 20231020000301.png|400]]
![[Pasted image 20231020000346.png|300]]

---
URL - Uniform Resource Locator
![[Pasted image 20231021180036.png|400]]

scheme (protocol)
![[Pasted image 20231021180219.png|300]]
![[Pasted image 20231021180247.png|300]]

domain
- second-level domain
- top-level domain
![[Pasted image 20231021180502.png|400]]
![[Pasted image 20231021180553.png|400]]
- com (commercial)
- org (organization)
- kz, ru, us, jp and etc (country) 
- gg - (game)

url path
![[Pasted image 20231021180820.png|400]]
![[Pasted image 20231021180848.png|400]]

url parameter 
![[Pasted image 20231021180929.png|400]]

query string
![[Pasted image 20231021180954.png|400]]
It begins with a question mark symbol and is placed after the URL Path. 
It contains parameters represented as key value pairs that can appear inside a URL path. 
You can add more than one by adding the ampersand symbol between parameters. 
Django can process both types of URL but mainly uses the URL parameters.

---
URL Design
Mapping URLs with Params

views.py
```python
def menuitems(request, dish):
    items = {
        'pasta': 'type of noodle',
        'falafel': 'deep fried patties r balls',
        'cheesecake': 'type of dessert',
    }
    description = items[dish]
    # word pasta is one of the dictionary items
    # text displays in the browser, formatted with the URL parameter as a heading and the dictionary description as text.
    return HttpResponse(f"<h2> {dish} </h2>" + description)
```

urls.py (app-level)
```python
from django.urls import path
from demoapp import views

urlpatterns = [
    path('dishes/<str:dish>', views.menuitems)
]
```

urls.py (project-level)
```python
from demoapp import views
from django.urls import include
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("demoapp.urls")),
]
```


![[Pasted image 20231021191018.png|400]]
For example, you can use a URL parameter to pass the primary key of a database table using the INT path convert type.


**Path converters**
The URL pattern treats the identifiers in angular brackets (<..>) as the path parameters. By default, it parses the received value to the string type. Other path converters available are:
- str - Matches any non-empty string and excludes the path separator, '**/**'. This is the default if a converter isn’t included in the expression.
- int - Matches zero or any positive integer and returns an int. For example:/customer/<int:id>
- slug - Matches any slug string consisting of ASCII letters or numbers, including the hyphen and underscore characters.
- uuid - Matches a formatted UUID.  For example: **075194d3-6885-417e-a8a8-6c931e272f00** and returns a UUID instance.
- path - Matches any non-empty string and includes the path separator, '/'.

Dynamic URLs path:
![[Pasted image 20231021220308.png|400]]

```python
urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name") ,
]
```


## Creating URLs and Views






## SRC

source:
[Creating views– official documentation](https://docs.djangoproject.com/en/4.1/topics/http/views/ "Django official documentation writing views page")
[Class-based views – Official](https://docs.djangoproject.com/en/4.1/topics/class-based-views/ "Class-based views page with examples")
[The render() function in Django](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#render "Django shortcut functions")
[Getting query parameters from a request in Django](https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters "URL dispatcher page")
[The HTTP server responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status "HTTP response status codes")


research:
- http request, response get post put delete function
- http response status codes
- http request and response (packets information)
- django urls mapping with parameters
- django app/views logic
- django object
- django URL Design
- django path and path converter 

