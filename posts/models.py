from django.db import models
from common.models import CommonModel

# Create your models here.
class Post(CommonModel):
  workplace = models.ForeignKey("workplaces.Workplace", on_delete=models.CASCADE, related_name="posts")
  category = models.ManyToManyField("categories.Category", related_name="posts")
  user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts")

  def categories(self):
    categories = []
    for name in self.category.values_list("name", flat=True):
      categories.append(name)
    return ", ".join(categories)

  def __str__(self):
    return f"{self.workplace} - {self.categories()}"
