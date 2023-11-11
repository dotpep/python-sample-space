from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu, name='menu and items of little lemon'),

    path('index/<str:name>/', views.index, name='index/your_name - write your name - get dict name key in html (Hello World in DTL) Using Dynamic URLs path.'),
    path('person/', views.person, name='person using dot notation'),
    
    path('login/', views.login, name='if admin login if not dont have admin access'),
    path('login_dynu/<str:name>/', views.login_dynamics_url, name='login_dynamic_urls'),

    path('langs/', views.my_view, name='with for loop nasted list programming language'),
    path('data/', views.data_view, name='data - for key, value in data.items'),
    path('nested/', views.nested_loop, name='nested loop'),

    path('additional/', views.additional, name='additional command DTL'),
    path('filters/', views.filters, name='filters in DTL')
]
