from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordContextMixin
from django.contrib.messages.views import SuccessMessageMixin


def authenticate_user(email, password):
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email, password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('landing_page')

        return render(request, 'login.html')


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    success_message = 'Account was created successfully.'


class UserUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('landing_page')
    template_name = 'update.html'
    success_message = 'User profile updated.'

    # This keeps users from accessing the profile of other users.
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    template_name = 'change_password.html'
    success_message = 'Password changed.'


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = 'password_change_done.html'
    title = _('Has??o zmienione pomy??lnie')


class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'
    success_message = 'Check your email for a reset link.'
