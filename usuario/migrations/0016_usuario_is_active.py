# Generated by Django 5.1.4 on 2024-12-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_remove_usuario_senha_alter_usuario_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
