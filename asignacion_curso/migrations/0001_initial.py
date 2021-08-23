# Generated by Django 3.2.6 on 2021-08-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Asignacion de cursos',
                'verbose_name_plural': 'Asignacion de cursos',
                'db_table': 'asignacion_curso',
            },
        ),
    ]
