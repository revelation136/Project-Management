# Generated by Django 4.1.5 on 2023-02-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0002_remove_manpower_name_manpower_first_manpower_last'),
    ]

    operations = [
        migrations.AddField(
            model_name='manpower',
            name='position',
            field=models.CharField(default='', max_length=64),
        ),
    ]
