from rest_framework import serializers
from seccion.models import Seccion
from curso.api.serializers import CursoSerializer
from user.api.serializers import UserSerializer

class SeccionListSerializser(serializers.ModelSerializer):
    course_code = CursoSerializer()
    username_professor = UserSerializer()
    class Meta:
        model=Seccion
        fields = ["id","section","year","status","course_code","start_time","end_time","username_professor","semester"]


class SeccionCreateSerializser(serializers.ModelSerializer):
    class Meta:
        model=Seccion
        fields = ["id","section","year","status","course_code","username_professor","start_time","end_time","semester"]