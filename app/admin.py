"""Django Admin for app"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                ),
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
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "is_staff",
        "is_superuser",
        "last_login",
        "date_joined",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("email",)


@admin.register(models.PetTag)
class PetTagAdmin(admin.ModelAdmin):
    """PetTag Admin"""

    list_display = (
        "tag",
        "code",
        "pet",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "pet",
        "pet__owner",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "tag",
        "code",
        "pet__name",
        "pet__owner__name",
        "pet__owner__email",
    )


@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Owner Admin"""

    list_display = (
        "name",
        "email",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "email",
    )


@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    """Pet Admin"""

    list_display = (
        "name",
        "owner",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "owner",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "owner__name",
        "owner__email",
    )
