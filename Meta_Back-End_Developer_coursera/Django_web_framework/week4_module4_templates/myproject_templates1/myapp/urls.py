from . import views
from django.urls import path
  
urlpatterns = [
    path('index/', views.index_example1, name='index'),
    path('index_var/', views.index_var, name='index variable'),

    path('about/', views.about),
]