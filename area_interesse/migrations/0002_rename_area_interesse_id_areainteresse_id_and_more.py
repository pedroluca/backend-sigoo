# Generated by Django 5.1.4 on 2024-12-24 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area_interesse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areainteresse',
            old_name='area_interesse_ID',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='areainteresse',
            old_name='area_interesse_nome',
            new_name='nome',
        ),
    ]
