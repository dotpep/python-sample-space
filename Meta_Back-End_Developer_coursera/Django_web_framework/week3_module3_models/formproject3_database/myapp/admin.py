from django.contrib import admin

# Register your models here.
from .models import Logger

admin.site.register(Logger)