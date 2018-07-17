# Generated by Django 2.0.5 on 2018-07-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tarea_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.Tipo'),
            preserve_default=False,
        ),
    ]