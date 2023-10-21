from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception): # request and exception is argument
    return HttpResponse('404: Page not Found! <br><br> <button onclick="location.href=\'/home/\';">Go to Homepage</button>')

def home(request):
    return HttpResponseNotFound(" Little Lemon !") # HttpResponseNotFound - 404