# Generated by Django 2.0.5 on 2018-06-01 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.Estado'),
            preserve_default=False,
        ),
    ]
