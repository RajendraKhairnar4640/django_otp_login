from django import forms
from django.forms import widgets
from .models import DirivingLicence
from django.contrib.admin.widgets import AdminDateWidget



class DateInput(forms.DateInput):
    input_type = 'date'

class DLForm(forms.ModelForm):

    class Meta:
        model = DirivingLicence

        fields = ['id','first_name','last_name','dob','place_of_birth','gender','address1','address2',
        'city','state','zipcode']

        widgets = {
            'dob': DateInput()
        }