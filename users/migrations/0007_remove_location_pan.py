# Generated by Django 4.2.4 on 2023-08-29 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_location_alter_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='pan',
        ),
    ]
