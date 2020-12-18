from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']