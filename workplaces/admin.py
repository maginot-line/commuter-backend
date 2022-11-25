from django.contrib import admin
from .models import Workplace, Occupation, Benefit

# Register your models here.
@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "occupations_list",
        "address",
        "work_days",
        "start_work_time",
        "off_work_time",
        "working_hours",
        "salary_type",
        "salary",
        "benefits_list",
    )

    list_filter = (
        "name",
        "occupations",
        "address",
        "work_days_of_week",
        "start_work_time",
        "off_work_time",
        "working_hours",
        "salary_type",
        "salary",
        "benefits",
    )

    search_fields = (
        "occupations",
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
                    "occupations",
                    "address",
                    "work_days_of_week",
                    "start_work_time",
                    "off_work_time",
                    "working_hours",
                    "salary_type",
                    "salary",
                    "benefits",
                )
            },
        ),
    )


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ("name",)

    list_filter = ("name",)

    search_fields = ("name",)

    fieldsets = (
        (
            "Occupation",
            {"fields": ("name",)},
        ),
    )


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ("name",)

    list_filter = ("name",)

    search_fields = ("name",)

    fieldsets = (
        (
            "Benefit",
            {"fields": ("name",)},
        ),
    )
