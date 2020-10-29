from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Post
# from .forms import AuthorChangeForm, AuthorCreationForm
# from django.contrib.auth.models import User
#
#
# class AuthorUserAdmin(UserAdmin):
#     add_form = AuthorCreationForm
#     form = AuthorChangeForm
#     model = User
#     list_display = ['email', 'username', 'is_staff', ]


admin.site.register(Post)
# admin.site.register(AuthorUserAdmin)