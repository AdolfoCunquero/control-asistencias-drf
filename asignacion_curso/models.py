from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from seccion.models import Seccion
from user.models import User

class AsignacionCurso(models.Model):
    section = models.ForeignKey(Seccion, on_delete=PROTECT)
    username_student = models.ForeignKey(User, on_delete=PROTECT)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.section.year)+'-'+self.section.course_code.course_code+'-'+self.section.section + ' '+ self.section.course_code.course_name

    class Meta:
        db_table = "asignacion_curso"
        unique_together = ('section', 'username_student')
        verbose_name = "Asignacion de cursos"
        verbose_name_plural = "Asignacion de cursos"
