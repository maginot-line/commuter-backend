from django.db import models
from common.models import CommonModel

# Create your models here.
class Company(CommonModel):
    name = models.CharField(max_length=100)
    avatar = models.FileField(blank=True)
    address = models.ForeignKey("addresses.Address", on_delete=models.CASCADE, related_name="companies")

    def __str__(self):
        return f"{self.name}"
