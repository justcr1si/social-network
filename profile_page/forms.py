from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
        )
