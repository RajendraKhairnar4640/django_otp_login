from django import forms
from django.forms import widgets
from .models import DirivingLicence
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
from myapp.validators import validate_file_size
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'

class DLForm(forms.ModelForm):
    captcha = CaptchaField()
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        age = (date.today() - dob).days / 365
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old')
        return dob

    class Meta:
        model = DirivingLicence

        fields = ['id','first_name','last_name','dob','place_of_birth','gender','address1','address2',
        'city','state','zipcode','image','file','captcha','comments','agree']

        widgets = {
            'dob': DateInput(),
            'comments':forms.Textarea(attrs={
                'rows':'10',
                'cols':'90',
                'minlength':'5',
                'maxlength':'20',
            }),

                   
        }

        help_texts = {
            'file': ("File Format must be..'pdf','doc','xlsx' and less than 10mb"),
            'image': ("File Format must be..'jpeg','png'"),
            'comments': ("The field must contain at least 20 characters"),
            'dob': ("You must be at least 18 years old'"),

        }

