# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A `CustomUser` class is created by inheriting from `AbstractUser`.
    We can then add new fields to the ones provided by `AbstractUser`.
    """

    registration_accepted = models.BooleanField(
        verbose_name="Registration Accepted",
        help_text=(
            "Designates whether user's registration has been accepted " "by an admin."
        ),
        default=False,
    )

    def __str__(self):
        """
        String representation of `CustomUser`.
        """
        return self.username
