# Generated by Django 3.1.2 on 2023-07-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idade',
        ),
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.TextField(default=2, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
    ]
