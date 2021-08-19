from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT
from seccion.api.serializers import SeccionListSerializser, SeccionCreateSerializser
from seccion.models import Seccion


class SeccionApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        seccion = Seccion.objects.all()
        serializer = SeccionListSerializser(seccion, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SeccionCreateSerializser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SeccionDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Seccion.objects.get(pk=pk)
        except Seccion.DoesNotExist:
            raise HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        section = self.get_object(pk)
        serializer = SeccionCreateSerializser(section)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        section = self.get_object(pk)
        serializer = SeccionCreateSerializser(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        section = self.get_object(pk)
        section.delete()
        return Response(status=HTTP_204_NO_CONTENT)
