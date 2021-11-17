from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
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
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email, password)
        context = {}

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html', context)
            else:
                context['error_message'] = "user is not active"
        else:
            context['error_message'] = "email or password not correct"

        return render(request, self.template_name, context)


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
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'
    success_message = 'Password changed.'


class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'
    success_message = 'Check your email for a reset link.'
