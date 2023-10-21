from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 4
def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of hot beverage',
        'lemonade': 'type of refreshment',
    }

    choice_of_drink = drink_name[drink]
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)


# 3
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


# 2 - errors
def showform(request):
    return render(request, "form.html") 


# 2.2 - errors
def getform(request): 
    if request.method == "POST": 
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        return HttpResponse("Name:{} UserID:{}".format(name, id))


# 1 (2 - urls (uniform resource locator)) mapping urls with params
name = "dot"
id = 1

def pathview(request, name, id):
    name = "dot"
    id = 1
    return HttpResponse("Name: {} \nUserID: {}".format(name, id))


def qryview(request): 
    name = request.GET.get('name', 'dot') 
    id = request.GET.get('id', '1')
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview_2(request, name=None, id=None): 
    name_request = request.GET.get('name', name) 
    id_request = request.GET.get('id', id)
    return HttpResponse("Name:{} UserID:{}".format(name_request, id_request)) 
