from rest_framework.viewsets import ModelViewSet
from curso.models import Curso
from rest_framework.permissions import IsAuthenticated
from curso.api.serializers import CursoSerializer

class CursoApiViewSet(ModelViewSet):
    #permission_classes= [IsAuthenticated]
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
