# Generated by Django 3.2.6 on 2021-08-23 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control_asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlasistencia',
            name='username_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='controlasistencia',
            unique_together={('date', 'username_student', 'asignation')},
        ),
    ]
