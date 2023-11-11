from django.shortcuts import render

# Create your views here.
def menu(request):
    menuitem = {'name': 'Greek salad'}
    newmenu = {
        'mains': [
            {'name': "falafel", 'price': "12"},
            {'name': "shawarma", 'price': "15"},
            {'name': "gyro", 'price': "10"},
            {'name': "pasta", 'price': "8"},
            {'name': "salad", 'price': "5"},
        ]
    }
    return render(request, 'menu.html', newmenu)



# readings
def index(request, name):
    content = {'name': name}
    return render(request, 'index.html', content)


def person(request):
    person_info  = {'name': 'Roger', 'profession': 'Teacher'}
    context = {'person': person_info}
    return render(request, 'person.html', context)


def login(request): 
    context = {'user':'admin'} 
    return render(request, 'login.html', context)


def login_dynamics_url(request, name):
    context = {'user': name}
    return render(request, 'login_dynamic_urls.html', context)


def my_view(request): 
    langs = ['Python', 'C#', 'C++', 'Rust', 'JavaScript', 'SQL', 'Java'] 
    return render(request, 'langs.html', {'langs':langs})


def data_view(request):
    data = {
        'name': 'Roger',
        'profession': 'Teacher',
        'hobby': 'Reading',
        'country': 'USA'
    }
    return render(request, 'data.html', {'data': data})


def nested_loop(request):
    dct = {'digits': ['One', 'Two', 'Three'],
           'tens': ['Ten', 'Twenty', 'Thirty']
           }
    return render(request, 'nested.html', {'dct': dct}) 


def additional(request):
    about = {'about': "additional command in DTL"}
    return render(request, 'additional.html', about)


def filters(request):
    my_filter = {
        'name': 'Alan Turing', 
        'key': '', 
        'words': ['Django', 'Template', 'Language'],
        'list': ["first", "second", "third", "fourth"], 
    }
    return render(request, 'filters.html', my_filter)