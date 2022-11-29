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
    address = models.ForeignKey("addresses.Address", on_delete=models.CASCADE, related_name="workplaces")
    work_days_of_week = models.ManyToManyField("workplaces.WorkDayOfWeek", related_name="workplaces")
    start_work_time = models.TimeField()
    off_work_time = models.TimeField()
    working_hours = models.IntegerField()
    salary_type = models.CharField(max_length=7, choices=SalaryTypeChoices.choices, blank=True)
    salary = models.PositiveIntegerField(blank=True, null=True)
    benefits = models.ManyToManyField("workplaces.Benefit", related_name="workplaces")

    def __str__(self):
        return f"{self.name}"

    def work_days(self):
        return f"{self.work_days_of_week.count()}"

    def benefits_list(self):
        benefits = []
        for name in self.benefits.values_list("name", flat=True):
            benefits.append(name)
        return ", ".join(benefits)


class WorkDayOfWeek(CommonModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Benefit(CommonModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
