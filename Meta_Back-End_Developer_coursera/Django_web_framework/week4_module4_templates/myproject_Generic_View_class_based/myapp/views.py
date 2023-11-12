from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.views.generic import View
from django.views.generic import TemplateView

from .models import Employee
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

###
class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__' 
    success_url = "/list" 
    template_name = 'employee_create.html'


class EmployeeList(ListView):
    model = Employee
    success_url = "/list"
    template_name = 'employee_list.html'


class EmployeeDetail(DetailView):
    model = Employee
    success_url = "/list"
    template_name = 'employee_detail.html'


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = "/list"
    template_name = 'employee_update_form.html'


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = "/list"
    template_name = 'employee_confirm_delete.html'


###

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


class IndexView_View(View):
    def get(self, request):
        template = loader.get_template('index.html')
        context = {}
        return HttpResponse(template.render(context, request))
    

class IndexView_Template(TemplateView):
    template_name = 'index.html'


