from django.db import models
from common.models import CommonModel

# Create your models here.
class Resume(CommonModel):
  post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='resumes')
  user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='resumes')
  content = models.TextField(max_length=1000, blank=True, null=True)
  is_confirm = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.post} - {self.user}'
