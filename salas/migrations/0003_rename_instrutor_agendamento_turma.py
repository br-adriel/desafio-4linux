# Generated by Django 4.0.4 on 2022-05-28 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0002_alter_sala_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='instrutor',
            new_name='turma',
        ),
    ]
