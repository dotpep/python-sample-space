from django.urls import path
from . import views

# genenerate api endpoint token 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Function based
    #path('menu-items', views.menu_items),
    #path('menu-items/<int:pk>', views.single_item),
    
    path('category',views.category, name='get all category'),
    path('category/<int:pk>',views.category_detail, name='get specific category-detail'),
    
    # Renderers
    path('menu', views.menu, name='template html renderer for display table of menu'),
    path('welcome', views.welcome, name='static html renderer to welcome'),
    path('menu-items-csv', views.csv_menu_items, name='csv renderers for display meny items'),
    
    # examples of Data Sanitization
    path('injection/', views.injection),
    
    # Class based
    path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
    
    # Token authentication
    path('secret/', views.secret),
    # generate token
    path('api-token-auth/', obtain_auth_token),
    
    # User roles
    path('manager-view/', views.manager_view),
    
    # Throttling
    path('throttle-check/', views.throttle_check),
    path('throttle-check-auth/', views.throttle_check_auth),
    
    # Throttling in Class-based views
    path('throttle-menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    path('throttle-menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
    
    # User account management with Djoser
    path('groups/manager/users', views.managers),
]
