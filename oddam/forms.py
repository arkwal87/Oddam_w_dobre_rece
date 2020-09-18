from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Donation


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="email")


class AjaxForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["quantity",
                  "categories",
                  "institution",
                  "address",
                  "phone_number",
                  "city",
                  "zip_code",
                  "pick_up_date",
                  "pick_up_time",
                  "pick_up_comment",
                  "user"]

