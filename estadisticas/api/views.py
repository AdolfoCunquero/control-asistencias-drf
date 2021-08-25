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
        # for item in ControlAsistencia.objects.raw(sql):
        #     data.append({
        #         "legend":item.legend,
        #         "conteo":item.conteo
        #     })

        return Response(data, status=HTTP_200_OK)

    def my_custom_sql(self, query):
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        return row



class EstadisticaPorCicloView(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        sql = '''
            SELECT 
                MAX(ca.id) AS id,
                s.semester,
                COUNT(0) AS asistencias
            FROM curso c
            INNER JOIN section s ON c.course_code = s.course_code_id
            INNER JOIN asignacion_curso a ON s.id = a.section_id
            INNER JOIN control_asistencia ca ON a.id = ca.asignation_id
            INNER JOIN user_user u ON u.id = s.username_professor_id
            WHERE c.status = 1 AND s.status = 1 AND a.status = 1 AND ca.status = 1 AND u.username = '{}'
            GROUP BY s.semester;
        '''.format(request.user)
        
        data =[]
        for item in ControlAsistencia.objects.raw(sql):
            data.append({
                "semester":item.semester,
                "asistencias":item.asistencias
            })

        return Response(data, status=HTTP_200_OK)


class EstadisticaPorEstudianteView(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        sql = '''
            SELECT 
                MAX(c.id) AS id,
                u.username,
                u.first_name,
                u.last_name,
                u.carnet,
                COUNT(0) AS asistencias
            FROM user_user u
            INNER JOIN asignacion_curso ac ON u.id = ac.username_student_id
            INNER JOIN section s ON ac.section_id = s.id
            INNER JOIN control_asistencia c ON c.username_student_id = u.id
            INNER JOIN user_user up ON up.id = s.username_professor_id
            WHERE u.rol_id = 3 AND ac.status = 1 AND c.status = 1  AND up.username = '{}'
            GROUP BY u.username, u.first_name, u.last_name, u.carnet;
        '''.format(request.user)
        
        data =[]
        for item in ControlAsistencia.objects.raw(sql):
            data.append({
                "username":item.username,
                "first_name":item.first_name,
                "last_name":item.last_name,
                "carnet":item.carnet,
                "asistencias":item.asistencias
            })

        return Response(data, status=HTTP_200_OK)
