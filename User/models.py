from django.contrib.auth.models import AbstractUser
from django.db import models


USER_TYPE = [
    (1, 'User'),
    (2, 'Instructor'),
]

class User(AbstractUser):
    cell_phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
    user_type = models.SmallIntegerField(choices=USER_TYPE, null=False, default=1)
    address1 = models.CharField(blank=True, default=' ', max_length=50, null=True)
    address2 = models.CharField(blank=True, default=' ', max_length=50, null=True)
    city = models.CharField(blank=True, default=' ', max_length=50, null=True)
    state = models.CharField(blank=True, default=' ', max_length=2, null=True)
    zipcode = models.CharField(blank=True, default=' ', max_length=5, null=True)


# Create your models here.
