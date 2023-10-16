## Project and Apps (Django)

mkdir buildDjango - create directory
cd buildDjango - change directory

python -m venv <name_venv> - setup venv py
source <name_venv>/bin/activate - activate virtual enviroment
#### In cmd.exe
<name_venv>\Scripts\activate.bat
#### In PowerShell
<name_venv>\Scripts\Activate.ps1

pip install <name_library> - install needed library for your project
python -m <name_library> version - check library install

pip install django
python -m django version

#### django

django-admin startproject <name_project> - create django project

python manage.py makemigrations
python manage.py migrate

python <manage.py> startapp <name_app> - create django app in (project_name) folder also add settings.py>INSTALLED_APPS='<name_app>', and start manage.py file in django project
python manage.py runserver - run django project


## Admin and Structure

#### django-admin and manage.py

django-admin startproject <name_project>
django-admin runserver
python manage.py runserver

#### app structures

python -m django startapp myapp

views.py 
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World - home page urls conf (myapp)')
```

urls.py
```python
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),]
```

views.py - logic of app (mapped url pattern, user-defined func and iteract with model and template)
urls.py - urls pattern defined with path() func


## Web Frameworks and MVT

web framework is solid foundation of project (fast dev, clean structure, change and modify, code reusability)
django is: fast, feature-rich, 

Three Tier Architecture - presentation tier(client), application tier(web and app server), data tier(db server)

DRY principles - don't repeat yourself
MVC frameworks architectur - model, view, secure, scalable
MVT architectur (django) - model(data), view(logic), template(display)

## SRC
source:
[Writing your first Django app – official documentation](https://docs.djangoproject.com/en/4.1/)
[MVT Framework - Django](https://docs.djangoproject.com/en/4.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)
[How to structure your Django project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

research topic:
- virtual environment python
- dry principles
- three tier architecture
- mvc architecture
- django mvt architecture
