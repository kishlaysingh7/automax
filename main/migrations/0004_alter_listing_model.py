# Generated by Django 4.2.4 on 2023-09-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_listing_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='model',
            field=models.CharField(max_length=60),
        ),
    ]
