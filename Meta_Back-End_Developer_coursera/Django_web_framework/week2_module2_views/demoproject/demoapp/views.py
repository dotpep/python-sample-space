from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 6(2 - requests and urls) demonstrates the attributes of the request and response objects. HTTP
def index(request):
    path = request.path
    method = request.method
    content = ''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method : {}</p>
</center> 
'''.format(path, method)
    return HttpResponse(content)



# 1 (1 - django views)
def home(request): 
    content = "<html><body><h1>Welcome to little lemon (func home)</h1></body></html>"
    return HttpResponse(content)

# 2
def say_hello(request):
    return HttpResponse("Hello World!")

# 3
def homepage(request):
    return HttpResponse("Welcome to homepage")

# time
# 4
from datetime import datetime 

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)


# 5
def menu(request):
    text = """
<h1 style="color: #F4CE14;"> This is little lemon - menu! </h1>
"""
    return HttpResponse(text)