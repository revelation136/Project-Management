# Generated by Django 4.1.7 on 2023-03-11 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payitem',
            name='contract_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payitem', to='projects.project'),
        ),
    ]
