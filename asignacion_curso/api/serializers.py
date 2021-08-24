from django.db.models import fields
from rest_framework import serializers
from asignacion_curso.models import AsignacionCurso
from user.api.serializers import UserStudentSerializer
from seccion.api.serializers import SeccionListSerializser

class AsignacionCursoListSerializer(serializers.ModelSerializer):
    section = SeccionListSerializser()
    username_student = UserStudentSerializer()
    class Meta:
        model = AsignacionCurso
        fields = ['id','section','username_student','status']


class AsignacionCursoStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionCurso
        fields = ['id','section','username_student','status']