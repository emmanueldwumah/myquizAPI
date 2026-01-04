from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserExtends(UserAdmin):
    list_display = ['username', 'first_name']

admin.site.register(CustomUser, CustomUserExtends)