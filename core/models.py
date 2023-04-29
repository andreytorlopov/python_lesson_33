from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    MEMBER = 'member', _("Member")
    MODERATOR = 'modeator', _("Moderator")
    ADMIN = 'admin', _("admin")


class User(AbstractUser):
    role = models.CharField(
        max_length=8, choices=UserRole.choices, default=UserRole.MEMBER)
