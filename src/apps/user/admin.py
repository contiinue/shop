from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdminForm(admin.ModelAdmin):
    list_display = ("username", "email", "date_joined", "is_staff")
