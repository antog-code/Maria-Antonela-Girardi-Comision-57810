# Generated by Django 5.0.6 on 2024-07-02 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_contactocliente_contactocoworking_experiencia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiencia',
            old_name='Empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='anioFin',
            new_name='fin',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='anioInicio',
            new_name='inicio',
        ),
    ]
