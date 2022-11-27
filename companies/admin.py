from django.contrib import admin
from .models import Company

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "avatar")
    search_fields = ("name",)
    fieldsets = (("Company", {"fields": ("name", "address", "avatar")}),)
