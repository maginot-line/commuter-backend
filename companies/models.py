from django.db import models
from common.models import CommonModel

# Create your models here.
class Company(CommonModel):
    class Meta:
        verbose_name_plural = "Companies"

    class CompanyTypeChoices(models.TextChoices):
        contractor = ("contractor", "Contractor")
        agency = ("agency", "Agency")

    name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=10, choices=CompanyTypeChoices.choices)
    avatar = models.FileField(blank=True)
    address = models.ForeignKey("addresses.Address", on_delete=models.CASCADE, related_name="companies")

    def __str__(self):
        return f"{self.company_type} - {self.name}"
