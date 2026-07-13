# backend/socials/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SocialAccount(models.Model):
    PLATFORM_CHOICES = (
        ("telegram", "Telegram"),
        ("instagram", "Instagram"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)

    # общий идентификатор аккаунта
    account_uid = models.CharField(max_length=100)

    # -------- INSTAGRAM --------
    access_token = models.TextField(null=True, blank=True)
    ig_user_id = models.CharField(max_length=50, blank=True, null=True)

    # -------- TELEGRAM --------
    bot_token = models.CharField(max_length=255, blank=True, null=True)
    chat_id = models.CharField(max_length=100, blank=True, null=True)

    # -------- ОБЩЕЕ --------
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.platform}: {self.account_uid}"
