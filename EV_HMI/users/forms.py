from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Company


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['homepage', 'logo', 'image']

