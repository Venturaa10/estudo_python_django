# Generated by Django 4.1 on 2024-06-16 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='data',
            new_name='data_fotografia',
        ),
    ]
