from django.db import models
from common.models import CommonModel

# Create your models here.
class Post(CommonModel):
    title = models.CharField(max_length=100)
    work_place = models.ForeignKey("workplaces.Workplace", on_delete=models.CASCADE, related_name="posts")
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="posts")
