from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', views.form_view, name='home'),
]