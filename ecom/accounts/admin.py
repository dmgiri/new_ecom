from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

# Register your models here.
# admin.site.register(Account)


class AccountAdmin(UserAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "username",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
    )

    list_display_links = (
        "email",
        "first_name",
        "last_name",
    )

    readonly_fields = ("last_login", "date_joined")
    ordering = ("date_joined",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
