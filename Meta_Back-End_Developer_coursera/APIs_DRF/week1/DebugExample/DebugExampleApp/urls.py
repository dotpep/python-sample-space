from django.urls import path
from . import views

urlpatterns = [
    path('even/', views.display_even_numbers),
    path('odd/', views.display_odd_numbers),
]