from django.urls import path
from demoapp import views


urlpatterns = [
    # dynamic url path
    path('dishes/<str:dish>', views.menuitems),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
]