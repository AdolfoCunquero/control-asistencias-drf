from rest_framework import serializers
from user.models import User
from control_asistencia.models import ControlAsistencia
from asignacion_curso.models import AsignacionCurso

class ControlAsistenciaStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlAsistencia
        fields = ["id","date","asignation","status"]