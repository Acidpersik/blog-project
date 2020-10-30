from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AuthorChangeForm, AuthorCreationForm
from .models import CustomUser


class AuthorUserAdmin(UserAdmin):
    add_form = AuthorCreationForm
    form = AuthorChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'birth_date', 'twitter_link', ]


admin.site.register(CustomUser, AuthorUserAdmin)