from django.contrib import admin

# Register your models here.
from .models import Drinks, DrinksCategory

admin.site.register(Drinks)
admin.site.register(DrinksCategory)
