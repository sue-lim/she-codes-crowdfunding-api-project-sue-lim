from django.db import models
from django.contrib.auth.models import AbstractUser

User = AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)

    pass

    def __str__(self):
        return self.username
