from django.contrib import admin
from .models import Workplace

# Register your models here.
@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
  list_display = (
      "name",
      "address",
      "work_days",
      "start_work_time",
      "off_work_time",
      "working_hours",
      "salary_type",
      "salary",
      "benefits",
  )

  list_filter = (
      "name",
      "address",
      "work_days_of_week",
      "start_work_time",
      "off_work_time",
      "working_hours",
      "salary_type",
      "salary",
      "benefit",
  )

  search_fields = (
      "working_hours",
      "salary_type",
      "benefits",
  )

  fieldsets = (
      (
          "Workplace",
          {
              "fields": (
                  "name",
                  "address",
                  "work_days_of_week",
                  "start_work_time",
                  "off_work_time",
                  "working_hours",
                  "salary_type",
                  "salary",
                  "benefit",
              )
          },
      ),
  )
