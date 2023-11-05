from django import forms

SHIFTS = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="Name", required=False)
    last_name = forms.CharField(max_length=100, label="Surname", widget=forms.Textarea(attrs={'rows': 2}))
    shift = forms.ChoiceField(widget=forms.RadioSelect, choices=SHIFTS)
    time_log = forms.TimeField(help_text="Enter the exact time")