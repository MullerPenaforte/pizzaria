# Generated by Django 3.1.2 on 2023-07-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0003_auto_20230703_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(default='00000000000', max_length=11),
        ),
    ]