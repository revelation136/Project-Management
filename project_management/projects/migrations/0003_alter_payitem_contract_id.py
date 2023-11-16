# Generated by Django 4.1.7 on 2023-03-11 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_payitem_contract_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payitem',
            name='contract_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payitem', to='projects.project'),
        ),
    ]