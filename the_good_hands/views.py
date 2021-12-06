from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import datetime
from django.shortcuts import render

# Create your views here.
from django.views import View

from accounts.models import CustomUser
from the_good_hands.models import Donation, Institution, Category


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all().aggregate(Sum('quantity'))
        donated_institutions = Donation.objects.filter(quantity__gt=0).distinct().count()
        return render(request, 'index.html', {'donations': donations['quantity__sum'],
                                              'donated_institutions': donated_institutions,
                                              'foundations': Institution.objects.filter(type='1'),
                                              'organisations': Institution.objects.filter(
                                                  type='2'),
                                              'local_collections': Institution.objects.filter(type='3')
                                              })


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'form.html', {'categories': Category.objects.all(),
                                             'institutions': Institution.objects.all()
                                             },)

    def post(self, request):
        quantity = request.POST.get('bags')
        categories = request.POST.getlist('categories')
        institution = Institution.objects.get(pk=int(request.POST.get('organization')))
        address = request.POST.get('address')
        phone_number = int(request.POST.get('phone').replace(" ", ""))
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        pick_up_date = request.POST.get('data')
        pick_up_time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')
        user = request.user
        instance = Donation.objects.create(quantity=quantity, institution=institution, address=address,
                                           phone_number=phone_number, city=city, zip_code=zip_code,
                                           pick_up_date=pick_up_date,
                                           pick_up_time=pick_up_time, pick_up_comment=pick_up_comment, user=user)
        for category in categories:
            instance.categories.add(category)
        return render(request, 'form-confirmation.html')


class UserPage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'profile.html', {'active_user': CustomUser.objects.filter(pk=request.user.id)})


class DonationView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'donations.html', {
            'received_donations': Donation.objects.filter(user=request.user.id).filter(is_taken=True).order_by(
                'pick_up_date'),
            'missed_donations': Donation.objects.filter(user=request.user.id).filter(is_taken=False).order_by(
                '-pick_up_date')
        })

