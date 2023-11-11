from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader


def index_example1(request):
    name = "pep1"
    return HttpResponse("<h1>Hello, {}. You're at the polls index.</h1> {}".format(name, "pep"))

def index_example2(request):
    template = loader.get_template('hello.html')
    context = {}
    return HttpResponse(template.render(context, request))


def index_var(request):
    context = {"name": 'Pep'}
    return render(request, "hello.html", context)

def about(request):
    about_txt = "This is the about page"
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
    about_content = {'about': about_txt, 'nums': nums_list}
    return render(request, "about.html", about_content)