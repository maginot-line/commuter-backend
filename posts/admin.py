from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = (
      "workplace",
      "categories",
      "user__company",
      "user",
      "created_at",
      "updated_at",
  )

  list_filter = ("workplace", "category")

  search_fields = ("workplace",)

  fieldsets = (
      (
          "Post",
          {"fields": ("workplace", "category", "user")},
      ),
  )

  def user__company(self, obj):
    return obj.user.company
