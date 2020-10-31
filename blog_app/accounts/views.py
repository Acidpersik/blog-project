from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import AuthorCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = AuthorCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'profile.html'


