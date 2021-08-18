from rest_framework import serializers
from curso.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["course_code","course_name","status"]