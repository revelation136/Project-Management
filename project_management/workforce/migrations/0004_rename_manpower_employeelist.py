# Generated by Django 4.1.5 on 2023-03-01 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0003_manpower_position'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manpower',
            new_name='EmployeeList',
        ),
    ]