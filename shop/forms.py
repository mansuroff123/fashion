from django import forms
from django.forms.widgets import TextInput
from .models import ColorModel

class ColorModelForm(forms.ModelForm):
    code = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'type': 'color'}),)

    class Meta:
        code = forms.CharField()
        model = ColorModel
        fields = '__all__'
