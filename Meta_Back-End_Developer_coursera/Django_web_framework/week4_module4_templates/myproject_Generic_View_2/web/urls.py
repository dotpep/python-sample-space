from django.urls import path
from . import views
from .views import PanFormView

urlpatterns = [
    path('pans/', PanFormView.as_view(), name='create_pan'),
]