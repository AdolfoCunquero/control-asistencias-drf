from django.contrib import admin
from control_asistencia.models import ControlAsistencia

@admin.action
def make_inactive(self, request, queryset):
    queryset.update(status=False)

@admin.action
def make_active(self, request, queryset):
    queryset.update(status=True)

@admin.register(ControlAsistencia)
class RolAdmin(admin.ModelAdmin):
    list_display = ['date','username_student','asignation','status']
    list_filter = ['username_student',]
    search_fields = ['username_student',]
    list_per_page = 10
    actions=[make_inactive,make_active,]
