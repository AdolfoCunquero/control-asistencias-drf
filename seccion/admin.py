from django.contrib import admin
from seccion.models import Seccion

@admin.register(Seccion)
class RolAdmin(admin.ModelAdmin):
    list_display = ['course_code','section','year','semester',"start_time","end_time",'username_professor','status']
