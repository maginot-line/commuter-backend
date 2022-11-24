from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile", {"fields": ("name", "phone", "mobile_carrier", "resident_registration_number", "phone_verified")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined"), "classes": ("collapse",)}),
    )

    list_display = ("username", "name", "phone", "mobile_carrier", "resident_registration_number", "phone_verified", "is_staff")
