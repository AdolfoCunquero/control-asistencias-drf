# Generated by Django 3.2.6 on 2021-08-18 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_rol_id_user_rol'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rol',
            options={'verbose_name': 'Rol', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]