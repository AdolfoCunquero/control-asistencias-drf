from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from asignacion_curso.models import AsignacionCurso
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from asignacion_curso.api.serializers import AsignacionCursoListSerializer, AsignacionCursoStoreSerializer
from rest_framework.response import Response

class AsignacionCursoView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return AsignacionCurso.objects.get(pk=pk)
        except AsignacionCurso.DoesNotExist:
            return HTTP_404_NOT_FOUND

    def get(self, request, format=None):
        asignaciones = AsignacionCurso.objects.all()
        serializer = AsignacionCursoListSerializer(asignaciones, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = AsignacionCursoStoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_format = AsignacionCursoListSerializer(self.get_object(serializer.data['id']))
            return Response(data=serializer_format.data, status = HTTP_200_OK)

        return Response(data = serializer.errors, status= HTTP_400_BAD_REQUEST)
        

class AsignacionCursoDetailView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return AsignacionCurso.objects.get(pk=pk)
        except AsignacionCurso.DoesNotExist:
            return HTTP_404_NOT_FOUND

    def get(self, request, pk, format =None):
        asignation = self.get_object(pk=pk)
        serializer = AsignacionCursoListSerializer(asignation)
        if asignation != HTTP_404_NOT_FOUND:
            return Response(data = serializer.data)

        return Response(status = HTTP_404_NOT_FOUND)
        

    def put(self, request, pk, format = None):
        asignation = self.get_object(pk = pk)
        serializer = AsignacionCursoStoreSerializer(asignation, data = request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_format = AsignacionCursoListSerializer(asignation)
            return Response(serializer_format.data, status= HTTP_200_OK)

        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        asignation = self.get_object(pk = pk)
        if asignation != HTTP_404_NOT_FOUND:
            asignation.delete()
            return Response(status=HTTP_200_OK)

        return Response(status=HTTP_404_NOT_FOUND)

        



