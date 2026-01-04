from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserExtends(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'othername' ,'phone']

admin.site.register(CustomUser, CustomUserExtends)