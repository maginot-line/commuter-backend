from django.contrib import admin
from .models import Address

# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "address_type",
        "address",
        "address_detail",
        "latitude",
        "longitude",
    )

    list_filter = ("address_type",)

    search_fields = ("address",)

    fieldsets = (
        (
            "Address",
            {
                "fields": (
                    "address_type",
                    "address",
                    "address_detail",
                    "latitude",
                    "longitude",
                )
            },
        ),
    )
