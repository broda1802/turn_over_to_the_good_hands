# Generated by Django 3.2.9 on 2021-12-04 16:16

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('the_good_hands', '0004_auto_20211204_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
