# Generated by Django 4.0.3 on 2022-03-05 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lavacao', '0003_remove_etapa_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('autorizada', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=120)),
                ('categoria', models.CharField(choices=[('SV', 'SUV'), ('PK', 'PICAPE'), ('AT', 'AUTOMOVEL'), ('VN', 'VAN')], default='AT', max_length=2)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lavacao.marca')),
            ],
        ),
    ]
