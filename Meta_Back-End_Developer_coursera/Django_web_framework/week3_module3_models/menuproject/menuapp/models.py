from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()

    # 2
    # django custom method - str represents a Dunder method prints a string
    def __str__(self):
        return self.name + " : " + self.cuisine


# add project settings.py for line: INSTALLED_APPS = 'menuapp.apps.MenuappConfig',
# migration - `python manage.py makemigrations` and `python manage.py migrate`

# `python manage.py shell`
# from menuapp.models import Menu
# returns all entries in database - `Menu.objects.all()` | returns: <QuerySet []>
# m = Menu.objects.create(name = 'pasta', cuisine = 'italian', price = 10)
# assigned this entry to an object `m`
# `Menu.objects.all()` | returns: <QuerySet [<Menu: Menu object (1)>]> one entry is insade database
# m = Menu.objects.create(name = 'taco', cuisine = 'mexican', price = 2)
# n = Menu.objects.create(name = 'taco', cuisine = 'mexican', price = 2)

# 2
# update
# p = Menu.objects.get(pk=2)
# p.cuisine = 'chinese'
# p.save()
# Menu.objects.all() | <QuerySet [<Menu: pasta : italian>, <Menu: taco : chinese>, <Menu: taco : mexican>]>