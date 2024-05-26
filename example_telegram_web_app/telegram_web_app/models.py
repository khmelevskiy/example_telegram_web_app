from django.db import models


class User(models.Model):
    telegram_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    user_data = models.TextField(null=True, blank=True)  # TextField to store JSON user data
    init_data = models.TextField(null=True, blank=True)  # TextField to store JSON init data

    def __str__(self):
        return self.username or self.telegram_id


class ClickHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    click_time = models.DateTimeField(auto_now_add=True)  # Time of click
    points_after_click = models.IntegerField()  # Points after click

    def __str__(self):
        return f"Click by {self.user.username or self.user.telegram_id} at {self.click_time}"
