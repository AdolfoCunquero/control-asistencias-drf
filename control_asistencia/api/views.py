from asignacion_curso.models import AsignacionCurso
from typing import AsyncGenerator
from rest_framework.views import APIView
from control_asistencia.models import ControlAsistencia
from rest_framework.generics import CreateAPIView, ListAPIView
from control_asistencia.api.serializers import ControlAsistenciaStoreSerializer,ControlAsistneciaListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.db import connection

class ControlAsistenciaView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ControlAsistenciaStoreSerializer

    def perform_create(self, serializer):
        serializer.save(username_student=self.request.user)
        return super().perform_create(serializer)


class ControlAsistenciaListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        sql = "CALL sp_obtener_asistencia_hoy('{}');".format(request.user)

        data =[]
        # with connection.cursor() as cursor:
        #     cursor.execute(sql)
        #     for row in cursor.fetchall():

        #         print (row)
        for item in ControlAsistencia.objects.raw(sql):
            data.append({
                "id":item.id,
                "username":item.username,
                "first_name":item.first_name,
                "last_name": item.last_name,
                "carnet":item.carnet,
                "course_code":item.course_code_id,
                "course_name": item.course_name,
                "section": item.section,
                "start_time": item.start_time,
                "end_time": item.end_time,
                "date": item.date
            })

        return Response(data)