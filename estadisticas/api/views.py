from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from control_asistencia.models import ControlAsistencia
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK

class EstadisticaPorCursoView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
    
        sql = '''
            SELECT 
                MAX(ca.id) AS id,
                c.course_code,
                c.course_name,
                s.year,
                s.section,
                s.semester,
				u.username,
                COUNT(0) AS asistencias
            FROM curso c
            INNER JOIN section s ON c.course_code = s.course_code_id
            INNER JOIN asignacion_curso a ON s.id = a.section_id
            INNER JOIN control_asistencia ca ON a.id = ca.asignation_id
			INNER JOIN user_user u ON u.id = s.username_professor_id
            WHERE c.status = 1 AND s.status = 1 AND a.status = 1 AND ca.status = 1 AND u.username = '{}'
            GROUP BY c.course_code, c.course_name, s.year, s.section, s.semester, u.username;
        '''.format(request.user)
        
        data =[]
        for item in ControlAsistencia.objects.raw(sql):
            data.append({
                "course_code":item.course_code,
                "course_name":item.course_name,
                "year":item.year,
                "section": item.section,
                "semester":item.semester,
                "asistencias":item.asistencias
            })

        return Response(data, status=HTTP_200_OK)



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
