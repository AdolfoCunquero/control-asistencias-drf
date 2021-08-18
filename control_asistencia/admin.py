from django.contrib import admin
from control_asistencia.models import ControlAsistencia

@admin.register(ControlAsistencia)
class RolAdmin(admin.ModelAdmin):
    list_display = ['date','username_student','asignation','status']
