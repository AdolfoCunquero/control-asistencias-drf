from django.db import models
from django.db.models.deletion import CASCADE
from user.models import User
from asignacion_curso.models import AsignacionCurso

class ControlAsistencia(models.Model):
    date = models.DateField()
    username_student = models.ForeignKey(User, on_delete=CASCADE)
    asignation = models.ForeignKey(AsignacionCurso, on_delete=CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "control_asistencia"
        unique_together = ('date', 'username_student','asignation')
        verbose_name = "Control Asistencia"
        verbose_name_plural = "Control Asistencias"
