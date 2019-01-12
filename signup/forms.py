from django import forms
from .models import *
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email Id'}),required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required=True, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Enter Password'}),required=True, max_length=50)

    class Meta():
        model = User
        fields = ['username','email', 'password']
