from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


# Register your models here.
@admin.register(User)
class UserModelAdmin(UserAdmin):
    pass
