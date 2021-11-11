from django.shortcuts import render

# Create your views here.
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class LandingPage(View):
    def get(self, request):
        return render(request, 'index.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonation(View):
    def get(self, request):
        response = render(request, 'form.html', )
        return response
