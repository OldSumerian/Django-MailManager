import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER, SERVER_EMAIL
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, ProfilePasswordRestoreForm
from users.models import User


class LoginView(CreateView):
    model = User
    form_class = UserLoginForm
    template_name = "users/user_login.html"
    success_url = reverse_lazy("mailmanager:client_list")
    # form_valid method is overridden to perform additional validation checks
    def form_valid(self, form):
        if not form.is_valid():
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)
    # form_invalid method is overridden to display error messages
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    # get_context_data method is overridden to add extra context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Авторизация"
        return context
    # success_url is overridden to redirect to a different page after successful login
    def get_success_url(self):
        return "/profile"
    # logout_view method is overridden to redirect to a different page after successful logout
    def logout_view(request):
        from django.contrib.auth import logout
        logout(request)
        return redirect("/login")
    # get_object method is overridden to return the current logged-in user
    def get_object(self, queryset=None):
        return self.request.user

def confirm_user(request, code):
    user = get_object_or_404(User, verification_code=code)
    user.is_active = True
    user.save()
    message = f'Ваша регистрация подтверждена!'
    send_mail('Регистрация подтверждена',
              message, from_email=EMAIL_HOST_USER,
              recipient_list=[user.email] )
    return redirect(reverse('users:login'))


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_registration.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.verification_code = token
        host = self.request.get_host()
        url = f"http://{host}/users/confirm/{token}/"
        send_mail("Подтверждение почты", f"Для подтверждения вашей почты перейдите по ссылке ниже!\n{url}",
                        SERVER_EMAIL, recipient_list=[user.email])
        user.save()
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("mailmanager:profile")

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordRestoreView(CreateView):
    model = User
    form_class = ProfilePasswordRestoreForm
    template_name = 'users/restore_password.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = get_object_or_404(User, email=email)
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=['password'])

        send_mail("Новый пароль",
                  f"Ваш новый пароль!\n{password}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])

        return redirect(self.success_url)
