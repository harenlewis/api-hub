from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator


class AuthForm(forms.Form):
    email = forms.CharField(max_length=256, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, validators=[
                               MaxLengthValidator(150, message="Username Name is too long.")])
    email = forms.EmailField(max_length=150, validators=[
                                     MaxLengthValidator(150, message="Email Address is too long")])
    password = forms.CharField(widget=forms.PasswordInput, validators=[
                                    MinLengthValidator(8, message="Password is too short.")])
