from django.shortcuts import render

from django.http import HttpResponse
from .models import Menu

# Create your views here.
def menu(request):
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


def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)
