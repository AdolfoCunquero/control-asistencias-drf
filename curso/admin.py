from django.contrib import admin
from curso.models import Curso

@admin.register(Curso)
class RolAdmin(admin.ModelAdmin):
    list_display = ['course_code','course_name','status']
