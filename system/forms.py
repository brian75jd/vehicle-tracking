from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class UserRegistration(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        'placeholder':'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password(atleast 8 characters)',
        'class':'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
        'class':'form-control'
    }))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UserLogging(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        'placeholder':'Username'
    }))


    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'form-control'
    }))
    class Meta:
        model = User
        fields = ('username','password')

class ProfileUpdate(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        'placeholder':'Phone'
    }))


    UserID = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'National ID number',
        'class':'form-control'
    }))
    class Meta:
        model = Client
        fields = ('phone','userID')

class CompleteProfile(forms.ModelForm):
    plate = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        'placeholder':'Vehicle plate number',
        'required':True
    }))


    type= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Vehicle type (eg Madza Cx5)',
        'required':True,
        'class':'form-control'
    }))
    color = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        'placeholder':'Vehicle color',
        'required':True
    }))
    class Meta:
        model = Vehicle
        fields = ('plate','type','color')