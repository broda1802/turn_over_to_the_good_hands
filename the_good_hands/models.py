from django.db import models
from localflavor.pl.forms import PLPostalCodeField
from phone_field import PhoneField
# Create your models here.
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


INSTITUTION_TYPES = [
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna')
]


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.SmallIntegerField(choices=INSTITUTION_TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.SmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField(max_length=128)
    phone_number = models.IntegerField(blank=True, help_text='Contact phone number')
    city = models.TextField(max_length=64)
    zip_code = models.IntegerField(null=True, blank=True)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=256)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.city


