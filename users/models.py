from django.db import models
from django.contrib.auth.models import User

from localflavor.in_.models import INStateField #INPANCardNumberField

from .utils import user_directory_path

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    #pan = INPANCardNumberField (default="NY")
    city = models.CharField(max_length=64)
    state = INStateField(default="NY")

    def __str__(self):
        return f'{self.id}'


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to= user_directory_path, null=True)
    bio=models.CharField(max_length=140,blank=True)
    phone_number = models.CharField(max_length=11,blank=True)
    Location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

