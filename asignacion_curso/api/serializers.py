from django.db.models import fields
from rest_framework import serializers
from asignacion_curso.models import AsignacionCurso
from user.api.serializers import UserSerializer
from seccion.api.serializers import SeccionListSerializser

class AsignacionCursoListSerializer(serializers.ModelSerializer):
    section = SeccionListSerializser()
    username_student = UserSerializer()
    class Meta:
        model = AsignacionCurso
        fields = ['id','section','username_student','status']


class AsignacionCursoStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionCurso
        fields = ['id','section','username_student','status']