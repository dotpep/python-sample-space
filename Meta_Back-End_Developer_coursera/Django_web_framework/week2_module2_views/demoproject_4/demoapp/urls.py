from django.urls import path

from django.urls import re_path
from . import views

# application namespace (The problem comes when the view function of the same name is defined in more than one app. This is where the idea of a namespace is needed.)
app_name = 'demoapp'

urlpatterns = [
    path('home/', views.home),

    path('menu_item/10', views.display_menu_item, name = "static_path"),
    re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item, name = "regex_dynamic_path/menu_item/0-99"),

    # 2
    path('', views.index, name = "index"), 
    path('login/', views.login, name = "login"),

]