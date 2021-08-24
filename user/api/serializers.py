from django.db import models
from django.db.models import fields
from rest_framework import serializers
from user.models import User
from user.models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["id","rol_name"]


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name','password','carnet','rol']

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","username","first_name","last_name", "rol"]

class UserStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","carnet","email","username","first_name","last_name", "rol"]


class UserUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","username","first_name","last_name","carnet","status"]


class UserListSerializer(serializers.ModelSerializer):
    rol = RolSerializer()
    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","carnet","rol","status"]
