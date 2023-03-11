# Generated by Django 4.1.7 on 2023-03-09 11:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_id', models.CharField(default='', max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]+$')])),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PayItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilization', models.IntegerField()),
                ('occupational_safety', models.IntegerField()),
                ('temporary_facility', models.IntegerField()),
                ('reinforce_concrete', models.IntegerField()),
                ('masonry_works', models.IntegerField()),
                ('steel_works', models.IntegerField()),
                ('contract_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
