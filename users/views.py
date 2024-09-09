from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm
from users.models import User


class LoginView(CreateView):
    model = User
    form_class = UserLoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("users:profile")