# Generated by Django 3.2.9 on 2021-12-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_good_hands', '0005_auto_20211204_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.IntegerField(blank=True, help_text='Contact phone number'),
        ),
    ]
