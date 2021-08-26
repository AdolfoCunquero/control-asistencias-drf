from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from control_asistencia.models import ControlAsistencia
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.renderers import JSONRenderer
from django.db import connection

class EstadisticaPorCursoView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, course_code, fecha, *args, **kwargs):
    
        sql = "CALL sp_estadisticas_por_curso('{}','{}','{}');".format(course_code,request.user, fecha)
        data =[]
        data_row = self.my_custom_sql(sql)
        
        for item in data_row:
            data.append({
                "legend": item[0],
                "conteo": item[1]
            })

        return Response(data, status=HTTP_200_OK)

    def my_custom_sql(self, query):
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        return row



class EstadisticaPorEstudianteView(ListAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, course_code, fecha, *args, **kwargs):
    
        sql = "CALL sp_estadistica_por_curso_detalle('{}','{}','{}');".format(course_code,request.user, fecha)
        data =[]
        data_row = self.my_custom_sql(sql)
        
        for item in data_row:
            data.append({
                "carnet": item[0],
                "first_name": item[1],
                "last_name": item[2],
                "date": item[3],
            })

        return Response(data, status=HTTP_200_OK)

    def my_custom_sql(self, query):
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        return row