from django import forms

from .models import Pan

class PanForm(forms.ModelForm):
    class Meta:
        model = Pan
        #fields = '__all__'
        fields = ['price', 'vendor', 'diameter']



    #class Meta:
    #    model = models.Pan
    #    fields = '__all__'
    #    exclude = ['user']
    #    widgets = {
    #        'name': forms.TextInput(attrs={'class': 'form-control'}),
    #        'description': forms.Textarea(attrs={'class': 'form-control'}),
    #        'price': forms.NumberInput(attrs={'class': 'form-control'}),
    #        'image': forms.FileInput(attrs={'class': 'form-control'}),
    #    }
    #    labels = {
    #        'name': 'Название',
    #        'description': 'Описание',
    #        'price': 'Цена',
    #        'image': 'Изображение',
    #    }
    #    help_texts = {
    #        'name': 'Название товара',
    #        'description': 'Описание товара',
    #        'price': 'Цена товара',}
        