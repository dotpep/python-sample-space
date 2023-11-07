from django.contrib import admin

# Register your models here.
from .models import Person 

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin 


#admin.site.register(Person) 
#admin.site.unregister(User)

if admin.site.is_registered(User):
    admin.site.unregister(User)


@admin.register(User) 
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 
    
@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name")