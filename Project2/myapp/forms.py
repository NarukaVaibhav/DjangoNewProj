from django import forms
from .models import InputData

class InputForm(forms.ModelForm):
    class Meta:
        model = InputData
        fields = ['input_field']
