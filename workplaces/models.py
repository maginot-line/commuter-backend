from django.db import models
from common.models import CommonModel

# Create your models here.
class Workplace(CommonModel):
    class SalaryTypeChoices(models.TextChoices):
        HOURLY = ("hourly", "시급")
        DAILY = ("daily", "일급")
        MONTHLY = ("monthly", "월급")
        YEARLY = ("yearly", "연봉")

    name = models.CharField(max_length=100)
    Occupation = models.ForeignKey("workplaces.Occupation", on_delete=models.CASCADE, related_name="workplaces")
    address = models.ForeignKey("addresses.Address", on_delete=models.CASCADE, related_name="workplaces")
    working_day = models.CharField(max_length=100)
    working_start_time = models.TimeField()
    working_end_time = models.TimeField()
    working_hours = models.IntegerField()
    salary_type = models.CharField(max_length=7, choices=SalaryTypeChoices.choices, blank=True)
    salary = models.PositiveIntegerField(blank=True, null=True)
    benefits = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Occupation(CommonModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
