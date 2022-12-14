from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
  list_display = (
      'post',
      'user',
      'content',
      'is_confirm',
      'created_at',
      'updated_at',
  )

  list_filter = ('post__workplace__name', 'user')

  search_fields = ('post__workplace__name', 'user')

  fieldsets = (
      (
          'Resume',
          {'fields': ('post', 'user', 'content', 'is_confirm')},
      ),
  )

  def post__workplace__name(self, obj):
    return obj.post.workplace.name
