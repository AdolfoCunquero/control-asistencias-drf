# Generated by Django 3.2.6 on 2021-08-23 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asignacion_curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlAsistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('asignation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignacion_curso.asignacioncurso')),
            ],
            options={
                'verbose_name': 'Control Asistencia',
                'verbose_name_plural': 'Control Asistencias',
                'db_table': 'control_asistencia',
            },
        ),
    ]
