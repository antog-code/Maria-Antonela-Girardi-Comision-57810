# Generated by Django 5.0.6 on 2024-07-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0018_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudios',
            old_name='anio',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='descripcion',
            field=models.TextField(max_length=300),
        ),
    ]
