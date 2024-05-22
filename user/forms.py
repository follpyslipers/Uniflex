from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class UserRegisterForm(UserCreationForm):
    matric_number = forms.CharField(
        label="Matric Number",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matric Number', 'required': True}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address', 'required': True}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'required': True}),
    )

    class Meta:
        model = User
        fields = ['matric_number', 'email', 'password1', 'password2']
