from django.forms import ModelForm 
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from app.models import (
    Student ,
)
from django.contrib.auth.models import User


class RegisterForm(ModelForm) : 
    password = forms.CharField( min_length=4,max_length=100 ,
     widget = forms.PasswordInput() ,
    )
    confirm_password = forms.CharField(min_length =4 , max_length=100 ,
        widget = forms.PasswordInput() ,
    )
    class Meta:
        model = Student
        fields = ['name', 'year_of_passing', 'dept']
    
    def clean(self):
        super(RegisterForm ,self).clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password : 
            print("Passwords do not match")
            raise forms.ValidationError(
                "passwords do not match"
            )
        return self.cleaned_data

    def clean_name(self) : 
        username = self.cleaned_data['name']
        try : 
            user = User.objects.get(username = username)
        except User.DoesNotExist : 
            return username
        print("Username already in use")
        raise forms.ValidationError(
            'Username already in use' 
        )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

   
class LoginForm(ModelForm) :
    password = forms.CharField(
        widget=forms.PasswordInput()
    ) 
    class Meta  : 
        model = Student
        fields =['name']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


