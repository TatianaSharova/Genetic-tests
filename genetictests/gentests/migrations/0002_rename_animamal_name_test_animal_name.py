# Generated by Django 4.2.17 on 2024-12-12 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gentests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='animamal_name',
            new_name='animal_name',
        ),
    ]
