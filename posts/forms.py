from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['task','completed']