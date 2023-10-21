from django.urls import path
from demoapp import views


urlpatterns = [
    path('<str:dish>', views.menuitems) 
]