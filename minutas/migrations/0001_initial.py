# Generated by Django 3.2.3 on 2021-05-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minuta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('secretario', models.CharField(max_length=150)),
                ('texto', models.CharField(max_length=5000)),
                ('fecha_reunion', models.CharField(max_length=10)),
                ('hora_inicio', models.CharField(max_length=5)),
                ('hora_fin', models.CharField(max_length=5)),
                ('asistentes', models.CharField(max_length=5000)),
            ],
        ),
    ]