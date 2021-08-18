from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from user.models import User, Rol

@admin.register(User)
class UserAdmin(UA):
    fieldsets = list(UA.fieldsets).append (
        (None, {'fields': ('rol')}),
    )   


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['rol_name']

# Register your models here.
