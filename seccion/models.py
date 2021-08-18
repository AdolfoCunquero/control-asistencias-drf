from django.db import models
from django.db.models.deletion import PROTECT
from curso.models import Curso
from user.models import User

class Seccion(models.Model):
    course_code = models.ForeignKey(Curso, on_delete=PROTECT)
    section = models.CharField(max_length=1, default='A')
    year = models.IntegerField()
    semester = models.IntegerField()
    username_professor = models.ForeignKey(User, on_delete=PROTECT)
    status = models.BooleanField(default=True)

    def __str__(self):
        #return self.section
        return str(self.year)+'-'+self.course_code.course_code+'-'+self.section+' '+self.course_code.course_name

    class Meta:
        db_table="section"
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"

