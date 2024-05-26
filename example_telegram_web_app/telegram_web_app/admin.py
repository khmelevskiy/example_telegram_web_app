from django.contrib import admin

from .models import ClickHistory, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_id",
        "first_name",
        "last_name",
        "username",
        "is_premium",
        "points",
        "user_data",
        "init_data",
    )
    search_fields = ("telegram_id", "username")


@admin.register(ClickHistory)
class ClickHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "click_time", "points_after_click")
    search_fields = ("user__telegram_id", "user__username")
