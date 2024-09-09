from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        labels = {
            'email': 'Адрес электронной почты',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'email': 'Введите адрес электронной почты.',
            'password1': 'Введите пароль.',
            'password2': 'Подтвердите пароль.',
        }


class UserLoginForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        labels = {
            'email': 'Адрес электронной почты',
            'password': 'Пароль',
        }
        help_texts = {
            'email': 'Введите адрес электронной почты.',
            'password': 'Введите пароль.',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
