# Generated by Django 4.1.5 on 2023-02-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manpower',
            name='name',
        ),
        migrations.AddField(
            model_name='manpower',
            name='first',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='manpower',
            name='last',
            field=models.CharField(default='', max_length=64),
        ),
    ]
