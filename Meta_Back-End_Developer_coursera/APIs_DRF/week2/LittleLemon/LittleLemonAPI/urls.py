from django.urls import path
from . import views

urlpatterns = [
    # class based
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('category', views.CategoryView.as_view(), name='get all category'),
    path('category/<int:pk>', views.SingleCategoryView.as_view(), name='get specific category-detail'),

    # function based
    #path('menu-items', views.menu_items),
    #path('menu-items/<int:pk>', views.single_item),
    #path('category',views.category, name='get all category'),
    #path('category/<int:pk>',views.category_detail, name='get specific category-detail'),
    
    # renderers
    path('menu', views.menu, name='template html renderer for display table of menu'),
    path('welcome', views.welcome, name='static html renderer to welcome'),
    path('menu-items-csv', views.csv_menu_items, name='csv renderers for display meny items'),
]
