# Generated by Django 5.1.4 on 2024-12-09 01:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bennyapp', '0002_rename_clientes_cliente_rename_juegos_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='plataforma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bennyapp.plataforma'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='j_p',
        ),
    ]
