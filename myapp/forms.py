from django import forms
from models import *
from django.contrib.auth import authenticate, login, logout, get_user_model

class DataForm(forms.Form):

    cam1 = forms.CharField(max_length=250)
    cam2 = forms.CharField(max_length=250)
    cam3 = forms.CharField(max_length=250)
    cam4 = forms.CharField(max_length=250)

    class Meta:
        fields = ['cam1', 'cam2', 'cam3', 'cam4']

