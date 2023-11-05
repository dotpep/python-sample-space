from django import forms

from django.forms.widgets import NumberInput

FAVORITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish'),
]


class DemoForm(forms.Form):
    name = forms.CharField(max_length=100, label="Enter name: ", widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailField(label="Enter email address: ")
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'})) # import forms.widgets NumberInput
    favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH, label="Select favorite dish: ")
    favorite_dish_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_DISH, label="Select favorite dish using radio: ")


class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 