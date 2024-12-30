# Generated by Django 5.1.4 on 2024-12-28 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_usuario_groups_usuario_is_active_usuario_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='area_interesse',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
