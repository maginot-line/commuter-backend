from django.db import models
from common.models import CommonModel

# Create your models here.
class Post(CommonModel):
    workplace = models.ForeignKey("workplaces.Workplace", on_delete=models.CASCADE, related_name="posts")
    occupations = models.ManyToManyField("posts.Occupation", related_name="workplaces")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts")

    def occupations_list(self):
        occupations = []
        for name in self.occupations.values_list("name", flat=True):
            occupations.append(name)
        return ", ".join(occupations)

    def __str__(self):
        return f"{self.workplace} - {self.occupations_list()}"


class Occupation(CommonModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
