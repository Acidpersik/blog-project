from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class AuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'age',)


class AuthorChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'age',)