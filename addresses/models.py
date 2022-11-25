from django.db import models
from common.models import CommonModel

# Create your models here.
class Address(CommonModel):
    class AddressTypeChoices(models.TextChoices):
        WORK = ("work", "근무지")
        COMPANY = ("company", "회사")

    address_type = models.CharField(max_length=7, choices=AddressTypeChoices.choices)
    address = models.CharField(max_length=100)
    address_detail = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.address_type} {self.address}"
