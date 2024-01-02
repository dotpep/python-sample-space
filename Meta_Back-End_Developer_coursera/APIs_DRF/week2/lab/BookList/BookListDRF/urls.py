from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
]
