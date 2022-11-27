from django.db import models
from common.models import CommonModel

# Create your models here.
class PersonInCharge(CommonModel):
    class Meta:
        verbose_name_plural = "People in charge"

    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="people_in_charge")
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
