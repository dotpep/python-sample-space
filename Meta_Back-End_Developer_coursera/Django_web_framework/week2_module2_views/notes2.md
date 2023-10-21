## View

#### http request and response

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
#### URL - Uniform Resource Locator
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
#### Mapping URLs with Params
URL Design

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


#### Path converters
The URL pattern treats the identifiers in angular brackets (<..>) as the path parameters. By default, it parses the received value to the string type. Other path converters available are:
- str - Matches any non-empty string and excludes the path separator, '**/**'. This is the default if a converter isn’t included in the expression.
- int - Matches zero or any positive integer and returns an int. For example:/customer/<int:id>
- slug - Matches any slug string consisting of ASCII letters or numbers, including the hyphen and underscore characters.
- uuid - Matches a formatted UUID.  For example: **075194d3-6885-417e-a8a8-6c931e272f00** and returns a UUID instance.
- path - Matches any non-empty string and includes the path separator, '/'.

#### Dynamic URLs path:
![[Pasted image 20231021220308.png|400]]

```python
urlpatterns = [
    re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item, name = "regex_dynamic_path/menu_item/0-99"),
]
```


## Creating URLs and Views

#### RegEx URLs
**Regular expressions in URLs:** 
RegEx, are a set of characters that specify a pattern and are used to search for or find patterns in a string.
![[Pasted image 20231021223428.png|400]]

```python
from django.urls import re_path
urlpatterns = [
    path('menu_item/10', views.display_menu_item, name = "static_path"),
    re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item, name = "regex_path"),
]
```
r - character r at the beginning, this makes a row string which treats the back slashes symbols as literal characters and not escape characters.
^ (caret symbol) -  used as the anchor at the start of the string, it can also be used for negation.
$ (dollar symbol) - which is used as the anchor for the end of the string.
[] (opening and closing square brackets) - to define a character set that matches any one of the characters present inside.
{} (curly brackets) - are used to specify the exact number of proceeding characters.
() (parenthesis) - are used for grouping parts of the RegEx.
![[Pasted image 20231021225228.png|400]]

---
#### URL Namespacing and Views

start the Django shell:
`python manage.py shell`
`django-admin shell`

Django’s reverse() function returns the URL path to which it is mapped.
```shell
>>> from django.urls import reverse 
>>> reverse('index') 
'/demo/'
```

The problem comes when the view function of the same name is defined in more than one app. This is where the idea of a `namespace` is needed.

##### Application namespace

The application namespace is created by defining `app_name` variable in the application’s `urls.py` and assigning it the name of the app. In the `demoapp/urls.py` script, make the change using the following code:
```python
#demoapp/urls.py
from django.urls import path  
from . import views    
app_name='demoapp' 
urlpatterns = [  
    path('', views.index, name='index'),      
]
```

The app_name defines the application namespace so that the views in this app are identified by it.
To obtain the URL path of the index() function, call the reverse() function by prepending the namespace to it.
```shell
>>> reverse('demoapp:index') 
'/demo/'
```

##### Instance namespace
You can also use the namespace parameter in the `include()` function while adding an app’s `urlpattern` to that of a project.
```python
#in demoproject/urls.py 
urlpatterns=[ 
    # ... 
    path('demo/', include('demoapp.urls', namespace='demoapp')), 
    # ... 
]
```
This namespace is called the `instance namespace`.


##### Using namespace in view
Suppose you want the user to be conditionally redirected to the login view from inside another view. You need to obtain the URL of the login view and send the control to it with `HttpResponsePermanentRedirect`.
```python
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 

def myview(request): 
    # .... 
    return HttpResponsePermanentRedirect(reverse('demoapp:login'))
```


##### namespace in the url tag
An HTML form is submitted to the URL specified in the action attribute.
```python
<form action="/demoapp/login" method="post"> 
#form attributes 
<input type='submit'> 
</form>
```
The form will then be processed by the view mapped to this URL. However, as mentioned above, a hard-coded URL is not desired. Instead, use the url tag of the Django Template Language. It returns the absolute path from the named URL.

Use the url tag to obtain the URL path dynamically, as shown below:
```python
<form action="{% url 'login' %}" method="post"> 
#form attributes 
<input type='submit'> 
</form>
```

Again, the login view may be present in multiple apps. Use the named URL qualified with the namespace to resolve the conflict.
```python
<form action="{% url 'demoapp:login' %}" method="post"> 
#form attributes 
<input type='submit'> 
</form>
```

#### Error Handling (in django)
![[Pasted image 20231022005354.png|400]]


Client Errors response 400-499 (file path issues):
- 400 (`bad request`) - represents a bad request. This occurs when parameters passed in the request are not what the server may expect.
- 401 - indicates that the user must log into an account before processing the request.
- 403 (`permission denied`) - indicating that the request was valid but that the Web server refuses to process it. This typically means that the user calling the resource does not have the required permissions to view the resource.
- 404 (`page not found`) - indicates that the requested resource was not found on the web server. This typically happens when the resource cannot be located at the specified file path.

Server Errors response 500-599 (Application failure or Response time limit exceeded):
- 500 (`Internal server error`, server or view)

##### Django Handle
django error handling file must be created at the project level to get applied across the project.
![[Pasted image 20231022010108.png|400]]

Further customization is possible by overriding the default values. fSuch values can be set in the root URL configuration file of your project. It's important to know that setting these variables in any other URL configuration file will have no effect.
![[Pasted image 20231022010901.png|400]]
![[Pasted image 20231022011249.png|400]]


**Custom error pages**
If you want to show your own error page whenever the user encounters a **404** error, you must create a **404.html** page and put it in the project/templates folder.


**Consider the following scenario, where you have a Product model in the app.**
The user wants the details of a product with a specific Product ID.
In the following view function, id is the parameter obtained from the URL.
It tries to determine whether any product with the given id is available. If not, the `Http404` exception is raised.
```python
from django.http import Http404, HttpResponse 
from .models import Product 

def detail(request, id): 
    try: 
        p = Product.objects.get(pk=id) 
    except Product.DoesNotExist: 
        raise Http404("Product does not exist") 
    return HttpResponse("Product Found")
```
Just like the `HttpResponseNotFound`, there are a number of other predefined classes such as `HttpResponseBadRequest`, `HttpResponseForbidden` and so on.


**Usually, the Django development server is in DEBUG mode, which shows the error's traceback instead of the exception.**
To render the custom exception message, the DEBUG variable in the project’s settings should be set to False.
```python
#settings.py  
# SECURITY WARNING: don't run with debug turned on in production!  
DEBUG = FALSE
```

views.py (project-level)
```python
from django.http import HttpResponse, HttpResponseNotFoun

def handler404(request, exception): # request and exception is argument
    return HttpResponse("404: Page not Found! <br><br> <button onclick="" href'';"">Go to Homepage")

def home(request):
    return HttpResponseNotFound(" Little Lemon !") # HttpResponseNotFound - 404
```

urls.py (project-level)
```python
from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('demo/', include("demoapp.urls")),
    path('newdemo/', include("newapp.urls")),
    # Instance namespace
    path('demo/', include('demoapp.urls', namespace='demoapp')),
    path('home/', views.home)
]

# custom view handling
handler404 = 'demoproject_4.views.handler404'
```

setting.py
```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*'] # * for include all posible hostsg
```


#### Class based View
- mvt design pattern
- robust solution 
- oop techniques (inheritance) (mixins or multiple inheritance)

Class based view allow to you use views as objects and offer an alternative to function based views.
![[Pasted image 20231022015353.png|400]]
Class based views, respond with different class instance methods to HTTP requests in place of writing conditional branches, such as using if else, statements inside the same function.
![[Pasted image 20231022015656.png|400]]
The advantage of using a class based view in this scenario, is that it allows you to remove the conditional logic to check the incoming request for the type of method.


**inheritance**
**mixins**

![[Pasted image 20231022020338.png|400]]

## SRC

source:
- [Creating views– official documentation](https://docs.djangoproject.com/en/4.1/topics/http/views/ "Django official documentation writing views page")
- [Class-based views – Official](https://docs.djangoproject.com/en/4.1/topics/class-based-views/ "Class-based views page with examples")
- [The render() function in Django](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#render "Django shortcut functions")
- [Getting query parameters from a request in Django](https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters "URL dispatcher page")
- [The HTTP server responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status "HTTP response status codes")

- [The django.urls functions for use in URLconfs - official documentation](https://docs.djangoproject.com/en/4.1/ref/urls/ "Django official documentation page django.urls functions for use in URLconfs")
- [URL dispatcher](https://docs.djangoproject.com/en/4.1/topics/http/urls/#url-dispatcher "Django official documentation page - URL dispatcher")
- [URLs - Official](https://docs.djangoproject.com/en/4.1/topics/http/urls/#how-django-processes-a-request "Django official documentation page - URL dispatcher page")
- [Regular Expressions](https://docs.djangoproject.com/en/4.1/topics/http/urls/#using-regular-expressions "Django official documentation page - Using regular expressions")
- [Django URL mapping](https://docs.djangoproject.com/en/4.1/topics/http/views/#mapping-urls-to-views "Django official documentation page - URL Dispatch with an overview on mappinger")
- [Get URL parameters in Django](https://docs.djangoproject.com/en/4.1/topics/http/urls/#how-django-processes-a-request "Django official documentation page - django.urls functions for use in URLconfs")
- [Render HTML Forms – GET and POST in Django](https://docs.djangoproject.com/en/4.1/topics/forms/ "Django official documentation page - working with forms")
- [HTTP Request Response object](https://docs.djangoproject.com/en/4.1/ref/request-response/ "Django official documentation page - request and response objects")

research:
- http request, response get post put delete function
- http response status codes
- http request and response (packets information)
- django urls mapping with parameters
- django app/views logic
- django object
- django URL Design
- django path and path converter 

- {% csrf_token %} in html
- /n /t f and r string in python code
- [Django Update Record (w3schools.com)](https://www.w3schools.com/django/django_update_record.php)
- mvt design pattern for django python project
- robust solution 
- oop inheritance in djnago project
- oop mixin in djnago project
