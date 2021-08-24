from django.db.models import fields
from rest_framework import serializers
from user.models import User
from control_asistencia.models import ControlAsistencia
from asignacion_curso.models import AsignacionCurso
from asignacion_curso.api.serializers import AsignacionCursoStoreSerializer


class ControlAsistenciaStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlAsistencia
        fields = ["id","date","asignation","status"]


class ControlAsistneciaListSerializer(serializers.ModelSerializer):
    asignation = serializers.ReadOnlyField(source='section')
    class Meta:
        model = ControlAsistencia
        fields = ["id","date","asignation","username_student"]
