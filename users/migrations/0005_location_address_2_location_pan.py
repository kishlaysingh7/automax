# Generated by Django 4.2.4 on 2023-08-29 19:37

from django.db import migrations, models
import localflavor.in_.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address_2',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='location',
            name='pan',
            field=localflavor.in_.models.INPANCardNumberField(default='NY', max_length=10),
        ),
    ]
