from django.urls import path
# 1
#from . import views
# dot (.) here indicates the same working directory as the file.
# 1.3
from demoapp import views

urlpatterns = [
    # 1 (1 - django views)
    path('', views.home),
    # 1.2
    path('home2', views.home)
]