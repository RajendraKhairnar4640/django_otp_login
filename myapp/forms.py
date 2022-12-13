from django import forms
from django.forms import widgets
from .models import DirivingLicence
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Layout, Submit, Div




class DateInput(forms.DateInput):
    input_type = 'date'

class DLForm(forms.ModelForm):

    class Meta:
        model = DirivingLicence

        fields = ['id','first_name','last_name','dob','place_of_birth','gender','address1','address2',
        'city','state','zipcode']

        widgets = {
            'dob': DateInput(),
        }

