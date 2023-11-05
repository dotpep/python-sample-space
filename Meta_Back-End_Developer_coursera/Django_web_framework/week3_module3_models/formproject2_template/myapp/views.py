from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.forms import InputForm

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)