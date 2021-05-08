from django import forms
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm

from . import models

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control','placeholder':'Create Password', 'autocomplete': 'new-password'}))
    password2 = forms.CharField( widget=forms.PasswordInput({'class': 'form-control','placeholder':'Confirm Password', 'autocomplete': 'new-password'}))

    class Meta:
        model = models.User
        fields = ['full_name', 'email', 'username', 'role','role_level','skills', 'interests' , 'password1', 'password2']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Full Name', 'title':'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email Address', 'title':'Email Address'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                              widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
