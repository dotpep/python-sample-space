## Templates
![[Pasted image 20231110223619.png|600]]
generate HTML dynamically
- static 
- dynamic 
![[Pasted image 20231110223728.png|500]]
render function handle dynamic content
![[Pasted image 20231110223853.png|500]]

---
![[Pasted image 20231110224138.png|400]]
DTL - django template language (adding dynamic content)
- variables - {{ content }}
- tags - {% content %}
- filters - 
- comments - {# this won't be rendered #}
- `{% csrf_token %}` - **csrf token** informs Django that the page visited is secure.
this is For Loop realization using tags and variable in DTL:
![[Pasted image 20231110224354.png|500]]

---
Template engine
![[Pasted image 20231110224719.png|300]]
![[Pasted image 20231110224734.png|400]]

---
Code Reuse by using templates
**Template Inheritance**
allows to build base template containing expected HTML elements of site and defines blocks that child templates can override. Once defined, all pages of the website can inherit the base template.
![[Pasted image 20231110225144.png|500]]
![[Pasted image 20231110225220.png|500]]
![[Pasted image 20231110225234.png|300]]

---
#### Rendering a Template

setup:
```python
# settings.py
INSTALLED_APPS = [
    "myapp",
]
# create templates directory in project level
# this define default template directory as in Project level (myapp, myproject, templates) 
TEMPLATES = [{
        'DIRS': ['templates'],
}]
```
```python
# myproject - urls.py
from django.urls import path, include
urlpatterns = [
    path('', include('myapp.urls'))
]
# myapp - urls.py
from . import views
from django.urls import path
urlpatterns = [
    path('index/', views.index),
]
```


render as `HttpResponse`
```python
from django.http import HttpResponse 
from django.template import loader 
def index(request): 
    template = loader.get_template('hello.html') 
    context={} 
    return HttpResponse(template.render(context, request))
```

using render function:
```python
from django.shortcuts import render 
return render(request, 'hello.html')
```

with giving variable for render function and creating dynamic html (using python dictionary):
```python
from django.shortcuts import render  
def index(request):  
    context={"name": "NoName"}  
    return render(request, 'hello.html', context)
```
```html
<h1>Hello {{ name }}</h1>  
```

tags:
```html
<h1> {% x for x in mylist %} </h1>
```

filters:
```html
{{ variable_name | filter_name }}
{{ name | upper }}
{{ name | lower }}
{{ name | title }}
```
```python
nums = [1,2,3,4]
string = 'Simple is better than complex'
nums = [1,2,3,4,5,6,7,8]
```
```html
{{ nums | length }} outputs 4
{{ string | wordcount }} returns 5
{{ nums | slice:"1:3" }} slicing
```
The **`first`** and **`last`** filters return the first and last item in the list.


---
**Creating Templates**
- model - is database
- view - retrieve data from database or data structure
- template - contain static html and dynamic data render (render function: request, path, dictionary)
![[Pasted image 20231110233455.png|500]]
![[Pasted image 20231110233604.png|500]]
variables as keys that template can display on dynamic way.

---
```python
def about(request):
    about_txt = "This is the about page"
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
    about_content = {'about': about_txt, 'nums': nums_list}
    return render(request, "about.html", about_content)
```
```html
    <h2> About </h2>
    <p> {{ about | upper }} </p>
    <p> {{ about | lower }} </p>
    <p> {{ about | title }} </p>
    <p> {{ about | wordcount }} </p>

    <p> {{ nums | length }} </p>
    <p> {{ nums | slice:"0::2" }} </p>
    <p> {{ nums | slice:"1:3" }} </p>
    <p> {{ nums | first }} </p>
    <p> {{ nums | last }} </p>
```

#### lab

fold name: project 
static image:
```python
# setting.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    'myapp/static',
]
```
```html
{% load static %}
<img src="{% static 'img/dessert.jpg' %}">
```


## Working with Templates
![[Pasted image 20231111011005.png|400]]
DTL - is based on Jinja2 (popular template engine used in Python) and DRY, Security

main syntax constructs in DTL
- variables
- tags
- filters
- comments


**variables** 
`{{ variable }}` - like dictionaries `{restaurant_name: 'Little Lemon'}`.
![[Pasted image 20231111011645.png|300]]

**tags** 
`{% variable %}` - logic that can you add to template like if and for loops.
- if - check login status using tags
![[Pasted image 20231111011941.png|400]]
- for - iterate over dictionary to display list, each item in list
![[Pasted image 20231111012208.png|200]]
![[Pasted image 20231111012259.png|400]]
- extends
- include

**filters**
`{{ variable | filter }}` - change values of variables.
![[Pasted image 20231111012647.png|400]]

**comments**
`{% comment "optional_note" %}`
`{% endcomment %}`

- `{# this won't be rendered #}`
- developers use comment for documentation
![[Pasted image 20231111012840.png|400]]


#### Template Language and Variable Interpolation

**Template Engine**
![[Pasted image 20231111182023.png|400]]

---
**Template Variable**

Assuming that the client URL is `http://localhost:8000/index/Novak`, the following view function receives the path parameter from the URL dispatcher and passes it as context to the template:
```python
# views.py
def index(request, name):       
    context={'name': name}   
    return render(request, 'index.html', context)

# urls.py in app level
urlpatterns = [
    path('index/<str:name>/', views.index, name='index'),
]
```
```html
<h2>Welcome {{ name | title }}</h2>
```
- if path url `/index/Novak` returns: Hello Novak

---
The value of any key in the context may be a singular object (string, integer), a list or a dictionary. 
A certain view passes a ‘person’ dictionary as a context.
```python
def person(request):
    person_info  = {'name': 'Roger', 'profession': 'Teacher'}
    context = {'person': person_info}
    return render(request, 'person.html', context)
```
```html
    <h2>Name: {{ person.name }}</h2>
    <h2>Profession: {{ person.profession }}</h2>
```
- Name: Roger 
- Profession: Teacher

---
**Template Tags**
- if
- for

---
```python
{% if expression == True %} 
HTML block 1 
{% else %} 
HTML block 2 
{% endif %}
```
```python
def login(request):
    context = {'user':'admin'}
    return render(request, 'login.html', context)
```
```html
    {% if user == "admin" %}
    <h2>Welcome {{ user }}</h2>
    {% else %}
    <h2>Welcome Guest. You dont have admin access</h2>
    {% endif %}
```

---
```python
def myview(request):
    langs = ['Python', 'C#', 'C++', 'Rust', 'JavaScript', 'SQL', 'Java']
    return render(request, 'langs.html', {'langs':langs})
```
```html
<h1>List of Languages</h1>
<ul>
    {% for lang in langs %}
    <li>{{ lang }}</li>
    {% endfor %}
</ul>
```
```html
<h1>Sorted List of Languages using forloop.counter</h1>
<ul>
    {% for lang in langs %}
    <li>{{ forloop.counter }} : {{ lang }}</li>
    {% endfor %}  
</ul>
```
- 1 : Python
- 2 : C#
- 3 : C++
`<li>{{ forloop.revcounter }} : {{ lang }}</li> `


```python
def data_view(request):
    data = {
        'name': 'Roger',
        'profession': 'Teacher',
        'hobby': 'Reading',
        'country': 'USA'
    }
    return render(request, 'data.html', {'data': data})
```
```html
    {% for key, value in data.items %}
    <h2>{{ key | title }}: {{ value }}</h2>
    {% endfor %}
```
- Name: Roger
- Profession: Teacher
- hobby: Reading
...

---
**Additional tags in DTL**

- `csrf_token`
- comment
- include
- with
- extends
```html
    <h4> % csrf_token % - form template as protection to prevent <br> Cross Site Request Forgeries (CSRF) <br> generates a token on the server-side</h4>
    <h3> {% csrf_token %} </h3>
    
    {% comment "this is my comment" %}
    <h4> {% csrf_token %} </h4>
    <p>This tag is used in a form template as protection to prevent Cross Site Request Forgeries (CSRF).
        This tag generates a token on the server-side to make sure to cross-check that the incoming requests do not contain the token.
        If found, they are not executed. </p>
    {% endcomment %}


    {% include "include_sample.html" %}

  
    {% comment "this is my comment" %}
    <h3> This tag sets a local variable that is available between % with % and % endwidth % tags. </h3>
    {% with rate = 5 %}
    Interest = { amt }*{{ rate }}
    {% endwith %}
    {% endcomment %}
```


---
**Filters**
`{{ variable | filter_name }}`

```python
def filters(request):
    my_filter = {
        'name': 'Alan Turing',
        'key': '',
        'words': ['Django', 'Template', 'Language'],
        'list': ["first", "second", "third", "fourth"],
    }

    return render(request, 'filters.html', my_filter)
```
```html
    <h4> {{ key | default:"in key of value there is nothing" | title }} </h4>

    <h4> {{ words | join:"_" | lower }} </h4>

    <h4> {{ name | upper }}  </h4>
    <h4> {{ name | wordcount }} </h4>
    <h4> {{ name | length }}  </h4>

    <h4> {{ list | first }} </h4>
    <h4> {{ list | last }} </h4>
```


#### Mapping model objects to a template (lab)

setup
```python
# settings.py
INSTALLED_APPS = [
    'myapp',
]
TEMPLATES = [
        'DIRS': ['templates'],
]
# urls.py (myproject-level)
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
# urls.py (myapplevel)
from . import views
from django.urls import path
urlpatterns = [
    path('menu_card/', views.menu_by_id, name='menu cards using Model (database)'),
]
# admin.py
from .models import Menu
admin.site.register(Menu)

```

model.py
```python
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
  
    def __str__(self):
        return self.name
```
views.py
```python
def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)
```
```html
{% if menu %}
{% for item in menu %}
{{ item.name | title}} : {{ item.price }}
<br>
{% endfor %}
{% else %}
<p> No Item to Display </p>
{% endif %}
```

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

#### Template inheritance
**Extends** - replaces content from the parent template.
extends tag create parent child relationship where child can overwrite parent functionality. 

**Include** - adds parts and includes rendering of a template in current content.

---
DRY - the framework, within reason, should deduce as much as possible from as little as possible.

template inheritance (using `include` tag in DTL)
![[Pasted image 20231111193729.png|500]]
![[Pasted image 20231111194137.png|500]]
![[Pasted image 20231111201438.png|600]]

---
- `include` - includes rendering a template in the current context
- `extends` - creates a parent child relationship where parent's functionality can be overwritten
- `with`

---
**include**
![[Pasted image 20231111195432.png|500]]
![[Pasted image 20231111195736.png|500]]
- include tag lets you either specify a template string or a variable to allow conditions for different rendering.
![[Pasted image 20231111201736.png|400]]
![[Pasted image 20231111201756.png|400]]
![[Pasted image 20231111201821.png|400]]

---
**extends**
- replace blocks or content from a parent template as opposed to include
![[Pasted image 20231111201954.png|500]]
![[Pasted image 20231111202012.png|500]]
![[Pasted image 20231111202058.png|500]]
- header to about html

#### DTL and Inheritance (lab)
Term inheritance is associated with the principle of **object-oriented programming**. It refers to the mechanism of a *child class inheriting the properties of its parent class*, and if required, extending or overriding them.
- Template inheritance is implemented with the `{% block %}` and `{% endblock %}` tags.
- Notice that the `{{ block.super }}` tag has been used. It is similar to Python’s `super()` function whereby you access the parent class methods in a child class. In the same way, the contents of the footer block will be rendered on the login page.

---
views.py
```python
def home(request):
    return render(request, 'home.html', {})

def register(request):
    return render(request, 'register.html', {})

def login(request):
    return render(request, 'login.html', {})
```
urls.py (myapp-level)
```python
from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
```
in myproject-level urls.py
```python
urlpatterns = [
    path('myapp/', include('myapp.urls')),
]
```
home.html
```html
{% extends "base.html" %}

{% block contents %}
<h2 align="center">This is Home page</h2>
{% endblock %}
```
register.html
```html
{% extends "base.html" %}

{% block contents %}
<h2 align="center">Registration Form appears here</h2>
{% endblock %}
```
login.html
```html
{% extends "base.html" %}

{% block contents %}
<h2 align="center">Login Form appears here</h2>
{% endblock %}

{% block footer %}
{{ block.super }}
<h4 align="right">Designed By: Alexa Designs Ltd</h4>
{% endblock %}
```
base.html
```html
    <!--header-->  
    <div style="height:10%;">  
    <h2 align="center">Django Web Application</h2>  
    <hr>  
    </div>

    <!--side bar-->
    <div style="width:20%; float:left; border-right-style:groove">
    <ul>
    <b>
    <li><a href="/myapp/home/">home</a></li>
    <li><a href="/myapp/register/">register</a></li>
    <li><a href="/myapp/login/">login</a></li>
    </b>
    </ul>
    </div>

    <!--contents-->  
    <div style="margin-left:21%;">  
    <p>  
    {% block contents %}  
    {% endblock %}
    </p>  
    </div>

    <!--footer-->
    <hr>

    {% block footer %}
    <div>
    <h4 align="right">All rights reserved</h4>  
    </div>
    {% endblock %}
```

**Static files** 
like images, JavaScript and csv, can be served by Django using the `{% static %}` tag
```python
{% load static %} 
<img src="{% static 'my_app/example.jpg' %}">
```


#### lab 2 (workplace)
settings.py
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = ["myproject/static",]
```
templates/menu.html
```html
{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> Menu</p>
<p> This is a Menu page for Little Lemon </p>
{% endblock %}
```
templates/index.html
```html
{% extends 'base.html'%}
{% load static %}
{% block content%}
<p> Home</p>
<p> This is the Home page for Little Lemon </p>
{% endblock %}
```
templates/book.html
```html
{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> Book</p>
<p> This is a Booking page for Little Lemon </p>
{% endblock %}
```
templates/about.html
```html
{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> About Us</p>
<p> This is an About page for Little Lemon </p>
{% endblock %}
```
templates/base.html
```html
    <!-- Add include tag -->
    {% include 'partials/_header.html' %}

    <main>
        <!-- Begin block content --> 
        {% block content%}
        {% endblock %}
        <!-- End block content -->
    </main>
```
partials/_header.html
```html
{% load static %}
<footer style="background-color: #EE9972; "></footer>
<header>
  <img src="{% static 'img/logo.png' %}" />
</header>

<nav>
    <ul>
      <li><a href="{% url 'home' %}">Home</a></li>
      <li><a href="{% url 'about' %}">About</a></li>
      <li><a href="{% url 'menu' %}">Menu</a></li>
      <li><a href="{% url 'book' %}">Book</a></li> 
    </ul>
</nav>
```
views.py
```python
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')
  
def book(request):
    return render(request, 'book.html')
```

## Debugging and Testing
web-project
- interlinked files
- dependencies
- troubleshooting difficulties
---
- not adding a view
- incorrect templates
- missing statements
- inaccessible resources

**don't run with debug turned on in production!**
- setting.py: DEBUG = True
- use third party library for testing
---
**Debugging** - remove application's errors and bugs.
**Testing** - metrics for quality, reliability, and performance. 

**Unit test** - isolate a function, class, or method and only test that piece of code.
![[Pasted image 20231112144920.png|400]]
![[Pasted image 20231112144939.png|400]]

---
#### Code example of Testing in Django

models.py 
```python
class Reservation_2(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
```
tests.py (myapp-level)
```python
from django.test import TestCase
# Create your tests here.
from .models import Reservation_2
from datetime import datetime

class ReservationTestCase(TestCase):
    
    def setUpTestData(cls):
        cls.reservation = Reservation_2.objects.create(
            first_name = "John",
            last_name = "McDonald"
        )
        
    def test_fields(self):
		 self.assertIsInstance(
			 self.reservation.first_name, str)
		self.assertIsInstance(
			self.reservation.last_name, str)
			
	def test_timestamps(self): 
		self.assertIsInstance(
			self.reservation.booking_time, datetime)
```
- `python manage.py makemigrations`
- `python manage.py migrate`
- after making migrations add `@classmethod` decorators:
```python
class ReservationTestCase(TestCase):

	@classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation_2.objects.create(
            first_name = "John",
            last_name = "McDonald"
        )
```
- `python manage.py test`
- return: `Ran 2 tests, OK`
- if `self.assertIsInstance(self.reservation.last_name, int)`
- return: `Ran 2 tests, FAILED (failures=1)`
- `FAIL: test_fields (myapp.tests.ReservationTestCase)` and `line 18, in test_fields self.assertIsInstance(self.reservation.last_name, int) AssertionError: 'McDonald' is not an instance of <class 'int'>`

#### Sub-classing Generic Views
`class_based` generic view
- declare class by extending `django.views.View` class and define `get()` and `post()` method inside it to handle HTTP requests.
- URL pattern connects class using `as_view()` method of View class.

example:
```python
#views.py
from django.views import View
class NewView(View):   
    def get(self, request):   
        # View logic will place here   
        return HttpResponse('response')
#urls.py 
from myapp.views import NewView   
urlpatterns = [   
    path('about/', NewView.as_view()),
]
```

Generic View:
- TemplateView
- CreateView 
- ListView
- DetailView 
- UpdateView 
- DeleteView
- LoginView

---
**Functional View** VS Generic View (class-based)
func view:
```python
from django.http import HttpResponse
from django.template import loader
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))
```
```python
from . import views
path('func/', views.index),
```
class view:
```python
from django.views.generic import View
class IndexView_View(View):
    def get(self, request):
        template = loader.get_template('index.html')
        context = {}
        return HttpResponse(template.render(context, request))
```
```python
from .views import IndexView_View
path('class/', IndexView_View.as_view()),
```

**Template View**
generic template view:
```python
from django.views.generic import TemplateView
class IndexView_Template(TemplateView):
    template_name = 'index.html'
```
```python
from .views import IndexView_Template
path('template', IndexView_Template.as_view())
```

---
**Requirements of a generic view**
- If the view needs a model to be processed, it should be set as the value of model property of the view.
- Each type of view looks for a template name with `modelname` suffixed by the type of generic view. For example, for a list view processing employee model, Django tries to find `employee_list.html`.
- The generic view is mapped with the URL with `as_view()` method of the View class.

**model.py Set Up**
Generic view classes to perform CRUD operations on the Employee model:
```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
  
    class Meta:  
        db_table = "Employee"
```
- make migrations
- `from .models import Employee` in views.py
- `from .views import *` in urls.py

**Create View**
```python
from django.views.generic.edit import CreateView
class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = "/list"
    template_name = 'employee_create.html'
```
```python
from .views import EmployeeCreate
path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
```
myapp/templates/employee_create.html
```html
<form method="post"> 
{% csrf_token %} 
<table> 
    {{ form.as_table }} 
</table> 
    <input type="submit" value="Save"> 
</form>
```

**List View**
```python
from django.views.generic.list import ListView  
class EmployeeList(ListView):   
    model = Employee   
    success_url = "/list"
    template_name = 'employee_list.html'
```
```python
from .views import EmployeeList
path('list/', EmployeeList.as_view(), name = 'EmployeeList'),
```
myapp/templates/employee_list.html
```html
<ul>  
    {% for object in object_list %}  
    <li>Name: {{ object.name }}</li>  
    <li>Email: {{ object.email }}</li>  
    <li>Contact: {{ object.contact }}</li>  
    <br/>
    {% endfor %}  
</ul>
```

**Detail View**
```python
from django.views.generic.detail import DetailView
class EmployeeDetail(DetailView):
    model = Employee
    success_url = "/list"
    template_name = 'employee_detail.html'
```
```python
from .views import EmployeeDetail
path('show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
```
myapp/templates/employee_detail.html
```html
<h1>Name : {{object.name}}</h1>

<p>Email : {{ object.email }}</p>
<p>Contact : {{ object.contact }}</p>
```

**Update View**
```python
from django.views.generic.edit import UpdateView
class EmployeeUpdate(UpdateView):   
    model = Employee   
    fields = '__all__'   
    success_url = "/list"
    template_name = 'employee_update_form.html'
```
```python
from .views import EmployeeUpdate
path('update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
```
myapp/templates/employee_update_form.html
```html
<form method="post"> 
{% csrf_token %} 
<table> 
    {{ form.as_table }} 
</table> 
    <input type="submit" value="Save"> 
</form>
```

**Delete View**
```python
from django.views.generic.edit import DeleteView
class EmployeeDelete(DeleteView):   
    model = Employee   
    success_url = "/list"
    template_name = 'employee_confirm_delete.html'
```
```python
from .views import EmployeeDelete
path('<delete/int:pk>', EmployeeDelete.as_view(), name = 'EmployeeDelete'),
```
myapp/templates/employee_confirm_delete.html
```python
<form method="post">
{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <input type="submit" value="Confirm">
</form>
```




## SRC
- django template language
- django template inheritance
- django testing and debugging
- class based generic views django

- how to work with django in pycharm
- django extensions in vs code (programming language, snippets)
- django Meta
- django Meta abstract class True
- django forms ModelForm
- django template logic include and expands
- django GET, POST terminal log


- dtl and template engine
- django code reuse
- [How to make a reusable template in Django? - Stack Overflow](https://stackoverflow.com/questions/9472034/how-to-make-a-reusable-template-in-django)
- django template and html and json
- is it possible to use django template and json
- how to parse or connect front end to django back end logic
- generic view in django
- generic edit createview in django
- [Generic editing views | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/)
- [Django Generic VIews - как просто формошлёпить - YouTube](https://www.youtube.com/watch?v=eVOjjVISFj0)

---
- [Testing in Django official](https://docs.djangoproject.com/en/4.1/topics/testing/ "Django official documentation page - Testing in Django")
- [Testing overview – Django official](https://docs.djangoproject.com/en/4.1/topics/testing/overview/ "Django official documentation page - Writing and running tests")
- [Django Advanced Testing topics](https://docs.djangoproject.com/en/4.1/topics/testing/advanced/#advanced-testing-topics "Django official documentation page - Advanced testing topics")
- [Django META header](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.META "Django official documentation page - Request and response objects")
- [Add unit testing to your Django project](https://docs.djangoproject.com/en/4.1/internals/contributing/writing-code/unit-tests/ "Django official documentation page - Unit tests")
- [Adding Django apps – Extended information](https://docs.djangoproject.com/en/4.1/ref/applications/ "Django official documentation page - Applications")
