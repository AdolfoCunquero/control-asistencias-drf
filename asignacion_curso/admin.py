from django.contrib import admin
from asignacion_curso.models import AsignacionCurso

@admin.register(AsignacionCurso)
class RolAdmin(admin.ModelAdmin):
    list_display = ['section','username_student','status']
