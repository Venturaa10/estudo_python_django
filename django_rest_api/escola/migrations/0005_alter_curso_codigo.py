# Generated by Django 5.1.2 on 2024-10-30 02:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_alter_estudante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
