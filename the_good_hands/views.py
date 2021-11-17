from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from django.views import View
from the_good_hands.models import Donation, Institution


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


class AddDonation(View):
    def get(self, request):
        response = render(request, 'form.html', )
        return response
