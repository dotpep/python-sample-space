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
- comments - 
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
**Additional command in DTL**

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


#### Mapping model objects to a template










## Debugging and Testing


## SRC
- 

---
- 
