from django.urls import path
from . import views
from .views import IndexView_View, IndexView_Template

from .views import EmployeeCreate, EmployeeList, EmployeeDetail, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('list/', EmployeeList.as_view(), name = 'EmployeeList'),
    path('show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name = 'EmployeeDelete'),

    ### 
    path('func/', views.index, name='index using func view'),
    path('class/', IndexView_View.as_view(), name='index class MyClass(View) using generic view (class based)'),
    path('template', IndexView_Template.as_view(), name='index class MyClass(TemplateView) using generic view (class based)'),
]