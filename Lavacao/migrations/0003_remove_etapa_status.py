# Generated by Django 4.0.3 on 2022-03-05 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lavacao', '0002_etapa_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etapa',
            name='status',
        ),
    ]