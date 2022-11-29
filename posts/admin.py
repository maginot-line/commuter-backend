from django.contrib import admin
from .models import Post, Occupation

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "workplace",
        "occupations_list",
        "user__company",
        "user",
        "created_at",
        "updated_at",
    )

    list_filter = ("workplace", "occupations")

    search_fields = ("workplace",)

    fieldsets = (
        (
            "Post",
            {"fields": ("workplace", "occupations", "user")},
        ),
    )

    def user__company(self, obj):
        return obj.user.company


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
