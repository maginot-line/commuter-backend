from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
  fieldsets = (
      (
          "Profile",
          {
              "fields": (
                  "name",
                  "phone_number",
                  "mobile_carrier",
                  "resident_registration_number",
                  "is_phone_number_verified",
                  "address",
                  "email",
                  "company",
                  "is_recruiter",
              )
          },
      ),
      (
          "Permissions",
          {
              "fields": (
                  "is_active",
                  "is_staff",
                  "is_superuser",
                  "groups",
                  "user_permissions",
              )
          },
      ),
      (
          "Important dates",
          {
              "fields": ("last_login", "date_joined"),
              "classes": ("collapse",),
          },
      ),
  )

  list_display = (
      "username",
      "name",
      "phone_number",
      "mobile_carrier",
      "resident_registration_number",
      "is_phone_number_verified",
      "company",
      "is_recruiter",
      "is_staff",
  )
