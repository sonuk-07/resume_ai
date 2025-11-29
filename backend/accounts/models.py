from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    resume_uploaded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.email})"
