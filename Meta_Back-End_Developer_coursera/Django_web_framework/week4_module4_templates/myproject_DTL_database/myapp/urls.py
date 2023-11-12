from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu_card/', views.menu_by_id, name='menu cards using Model (database)'),
]