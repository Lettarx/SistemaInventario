# Generated by Django 4.1.3 on 2022-12-03 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventarioAPP', '0003_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('rol_rolId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='InventarioAPP.rol')),
            ],
        ),
    ]
