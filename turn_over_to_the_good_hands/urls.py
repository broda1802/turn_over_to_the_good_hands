"""turn_over_to_the_good_hands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from the_good_hands.views import LandingPage, AddDonation, UserPage, DonationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('profile/', UserPage.as_view(), name='user_page'),
    path('donations/', DonationView.as_view(), name="donations"),
    path('', LandingPage.as_view(), name='landing_page'),
    path('add_donation', AddDonation.as_view(), name='add_donation'),
]
