from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

class UsuarioEdicionForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'imagen']
