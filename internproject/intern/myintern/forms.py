from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from django.forms.widgets import TimeInput
from .models import Report
from django import forms


# This is form report form

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReportForm(ModelForm):
    class Meta:
        labels = {
        "location": "Location ",
        "department": "Incident Department ",
        "date": "Date of Incident ",
        "time": "Time of Incident ",
        "incidentlocation": "Incident Location ",
        "saverity": "Initial Severity ",
        "cause": "Suspected Cause ",
        "actiontaken": "Immediate action taken:",
        "enviromentalincident":"Environmental incident",
        "injuryillness":"Injury / Illness",
        "propertydamage":"Property Damage",
        "vehicle":"Vehicle",



    }
        model = Report
        fields = ['location', 'department', 'date', 'time', 'incidentlocation', 'saverity', 'cause', 'actiontaken',
        'enviromentalincident','injuryillness','propertydamage','vehicle']
        widgets = {
            # 'location':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.Textarea(attrs={'class':'form-control', 'rows':4,'cols':50}),
            'date':DateInput(),
            'time':TimeInput(),
            'incidentlocation':forms.Textarea(attrs={'class':'form-control','rows':4,'cols':50,}),
            'cause':forms.Textarea(attrs={'class':'form-control','rows':4,'cols':50}),
            'actiontaken':forms.Textarea(attrs={'class':'form-control','rows':4,'cols':50}),
            

        }  


#  for register
# 

class signupForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name':'First Name', 'last_name':'Last Name',
        'email':'Email'}
        widgets = {

        'username' : forms.TextInput(attrs={'class':'form-control'}),
        'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),

        }



 # for login
class loginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))
