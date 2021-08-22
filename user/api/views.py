import django
from django.db.models import query
from rest_framework import response
import rest_framework
from rest_framework.generics import ListAPIView
from user.models import User, Rol
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerialier, RolSerializer, UserListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend


class RolView(ListAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]    
     
class AllUserListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rol__id']

class RegisterView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(status = status.HTTP_400_BAD_REQUEST, data = serializer.errors)

class UserView(APIView):
    permission_classes =[IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, pk, format=None):
        section = User.objects.get(pk=pk)
        section.delete()
        return Response(status=status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserUpdateSerialier(user, request.data) 

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


        