from rest_framework import serializers
from seccion.models import Seccion
from curso.api.serializers import CursoSerializer

class SeccionListSerializser(serializers.ModelSerializer):
    course_code = CursoSerializer()
    class Meta:
        model=Seccion
        fields = ["id","section","year","status","course_code","username_professor","semester"]


class SeccionCreateSerializser(serializers.ModelSerializer):
    class Meta:
        model=Seccion
        fields = ["id","section","year","status","course_code","username_professor","semester"]