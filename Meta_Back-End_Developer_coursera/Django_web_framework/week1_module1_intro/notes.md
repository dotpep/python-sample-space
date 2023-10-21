## Project and Apps (Django)

`mkdir buildDjango` - create directory
`cd buildDjango` - change directory

`python -m venv <name_venv>` - setup venv py
source <name_venv>/bin/activate - activate virtual enviroment

**In cmd.exe**
`<name_venv>\Scripts\activate.bat`
**In PowerShell**
`<name_venv>\Scripts\Activate.ps1`

`pip install <name_library>` - install needed library for your project
`python -m <name_library> version` - check library install

`pip install django`
`python -m django version`

#### django

`django-admin startproject <name_project>` - create django project

`python manage.py makemigrations`
`python manage.py migrate`

`python <manage.py> startapp <name_app>` - create django app in (project_name) ==folder also add settings.py>INSTALLED_APPS='<name_app>', and start manage.py file in django project and app should be in project folder with manage.py scripts==
`python manage.py runserver` - run django project


## Admin and Structure

#### django-admin and manage.py

`django-admin startproject <name_project>`
`django-admin runserver`
`python manage.py runserver`

#### app structures

`python -m django startapp myapp`

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

**views.py** - logic of app (mapped url pattern, user-defined func and iteract with model and template)
**urls.py** - urls pattern defined with path() func

django apps used to implement functionality(systems) for some specific purpose. 
![[Pasted image 20231019233752.png|300]]
functionality
![[Pasted image 20231019234011.png|300]]
dry principles
![[Pasted image 20231019234037.png|300]]
social media apps (project)
![[Pasted image 20231019234124.png|300]]
app contain
![[Pasted image 20231019234307.png|300]]

## Web Frameworks and MVT
web framework is solid foundation of project (fast dev, clean structure, change and modify, code reusability)
django is: fast, feature-rich, secure, scalable

**Three Tier Architecture** - presentation tier(client), application tier(web and app server), data tier(db server)
![[Pasted image 20231019234512.png|400]]

---

**DRY principles** - don't repeat yourself
**MVC frameworks architectur** - model, view, controller
**MVT architectur (django)** - model(data), view(logic), template(display)
![[Pasted image 20231019232308.png|400]]

---

About Django:
- is open source project written in python.
- excellent for projects that require high volumes (text content, media files, heavy traffic).
- works with (Templates, Libraries, APIs).
![[Pasted image 20231019232630.png|400]]
- area of using (ML and AI, Scalable web apps, SaaS apps, OTT platforms).
- cloud-storge apps (asynchronous views).

---

![[Pasted image 20231019234539.png|300]]
![[Pasted image 20231019234630.png|300]]





## SRC
source:
- [Writing your first Django app – official documentation](https://docs.djangoproject.com/en/4.1/)
- [MVT Framework - Django](https://docs.djangoproject.com/en/4.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)
- [How to structure your Django project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

research topic:
- virtual environment python
- dry principles
- three tier architecture
- mvc architecture
- django mvt architecture
