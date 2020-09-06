from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email / Username")
