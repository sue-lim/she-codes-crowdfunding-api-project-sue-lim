from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .import models
from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser


# Register your models here.
admin.site.register(models.CustomUser)
