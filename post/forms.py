
from django.forms import ModelForm 
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from app.models import (
    Company ,
    Domain ,
)

class PostForm(ModelForm):
    company = forms.ModelChoiceField(queryset= Company.objects.all() )
    intern = forms.BooleanField(initial=False ,required=False)
    ctc = forms.IntegerField()


    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self  , offer_id ,**kwargs) : 
        self.clean()
        self.instance.offer_id = offer_id
        return super(PostForm ,self).save(**kwargs)
    

