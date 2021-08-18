from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import PROTECT

class Rol(models.Model):
    rol_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.rol_name

    class Meta:
        verbose_name_plural = "Roles"
        verbose_name = "Rol"


class User(AbstractUser):

    carnet = models.CharField(blank=True,null=True, max_length=20)
    status = models.BooleanField(blank=False, default=True)
    rol = models.ForeignKey(Rol, on_delete=PROTECT, null=True)

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"
    #email = models.EmailField(unique=True)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

