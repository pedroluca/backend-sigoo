# Generated by Django 5.1.4 on 2025-01-08 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orientacao', '0002_orientacao_solicitacaoaceita'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientacao',
            name='foiSolicitada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orientacao',
            name='solicitacaoRecusada',
            field=models.BooleanField(default=False),
        ),
    ]
