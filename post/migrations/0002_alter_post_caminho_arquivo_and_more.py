# Generated by Django 5.1.4 on 2024-12-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caminho_arquivo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='horario_publicacao',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
