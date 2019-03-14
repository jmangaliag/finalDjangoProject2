from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from django import forms
from .models import Post

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id', 'is_active', 'date_modified', 'date_posted']
        widgets = {'posted_by': forms.HiddenInput()}
