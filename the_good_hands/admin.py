from django.contrib import admin

# Register your models here.
from the_good_hands.models import Category, Institution, Donation

admin.register(Category)
admin.register(Institution)
admin.register(Donation)
