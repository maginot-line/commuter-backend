from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  class MobileCarrierChoices(models.TextChoices):
    SKT = ("SKT", "SKT")
    KT = ("KT", "KT")
    LGU = ("LGU", "LGU")

  class GenderChoices(models.TextChoices):
    MALE = ("male", "Male")
    FEMALE = ("female", "Female")

  phone_number = models.CharField(max_length=20, blank=True)
  mobile_carrier = models.CharField(max_length=3, choices=MobileCarrierChoices.choices, blank=True)
  resident_registration_number = models.CharField(max_length=20, blank=True)
  gender = models.CharField(max_length=6, choices=GenderChoices.choices, blank=True)
  name = models.CharField(max_length=20, blank=True)
  is_phone_number_verified = models.BooleanField(default=False)
  address = models.ForeignKey("addresses.Address", on_delete=models.CASCADE, related_name="users", blank=True, null=True)
  email = models.EmailField(blank=True)
  avatar = models.FileField(blank=True)
  company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="users", blank=True, null=True, default=None)
  is_recruiter = models.BooleanField(default=False)
