from django.contrib import admin

# Register your models here.
from the_good_hands.models import Category, Institution, Donation

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)
