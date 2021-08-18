from django.db import models

class Curso(models.Model):
    course_code = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(unique=True, max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.course_code + ' ' + self.course_name

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        db_table = "curso"