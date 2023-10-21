"""
URL configuration for demoproject_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from demoapp import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1 angle brackets for define dynamic URL path (path converter)
    path('getuser/<str:name>/<int:id>', views.pathview, name='pathview'), 
    # 2
    path('getuser/', views.qryview, name='qryview') ,
    # (2) 3 - errors
    path("showform/", views.showform, name="showform"), 
    # (2.2) 3 - errors
    path("getform/", views.getform, name='getform'),
    # 4
    path('', include("demoapp.urls")),
]
