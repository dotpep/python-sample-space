from django.contrib import admin

# Register your models here.
from myapp.models import Reservation

#admin.site.register(Reservation)
    
@admin.register(Reservation) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("name", "contact", "date_time", "count_quest", "notes")