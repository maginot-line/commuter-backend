from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    mobile_carrier = models.CharField(max_length=20, blank=True)
    resident_registration_number = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20, blank=True)
    phone_verified = models.BooleanField(default=False)
