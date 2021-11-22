from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from django.views import View
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
                                             'list': list(Institution.objects.all())
                                             },)
