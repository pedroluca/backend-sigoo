# Generated by Django 5.1.4 on 2024-12-26 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_rename_id_usuario_id_remove_usuario_senha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='id',
            new_name='ID',
        ),
    ]
