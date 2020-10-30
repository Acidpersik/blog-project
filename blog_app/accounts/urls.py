from django.urls import path

from .views import SignUpView, CustomUserDetailView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('accounts/<int:pk>/profile', CustomUserDetailView.as_view(), name='user-profile'),

]
