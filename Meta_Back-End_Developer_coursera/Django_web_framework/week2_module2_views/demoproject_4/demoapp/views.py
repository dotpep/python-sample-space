from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 4 Namespace in view
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


# 5 Handling Errors in Views 
from django.http import HttpResponseNotFound
def my_view(request):
    if condition == True:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')
    
    #if condition == True: 
    #    return HttpResponse('<h1>Page not found</h1>', status_code='404') 
    #else: 
    #    return HttpResponse('<h1>Page was found</h1>') 




# 4 Namespace in view
def myview(request):
    return HttpResponsePermanentRedirect(reverse('demoapp:login'))

# 
def myform(request):
    return HttpResponse('')

# 3

def login(request):
    return HttpResponse("login")

def index(request):
    return HttpResponse("index")


def home(request):
    return HttpResponse("welcome to homepage")

def display_menu_item(request):
    return HttpResponse('in process of dev')