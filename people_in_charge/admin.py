from django.contrib import admin
from .models import PersonInCharge

# Register your models here.
@admin.register(PersonInCharge)
class PersonInChargeAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "phone_number", "email")

    list_filter = ("company__name",)

    search_fields = ("name",)

    fieldsets = (("Person in charge", {"fields": ("company", "name", "phone_number", "email")}),)
