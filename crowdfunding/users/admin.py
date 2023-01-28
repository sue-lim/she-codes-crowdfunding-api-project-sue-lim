from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .import models
from .models import CustomUser

# Register your models here, which will display - http://127.0.0.1:8000/admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(models.CustomUser)
