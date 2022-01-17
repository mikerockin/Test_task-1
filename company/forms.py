from django.forms import ModelForm
from .models import Employe, Subdivision
from django import forms


class EmployeForm(forms.ModelForm):

    class Meta:
        model = Employe
        fields = ('first_name', 'second_name', 'third_name', 'subdivision', 'department', 'position', 'date_of_employment',)

class SubvisionForm(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = ('name',)