# Generated by Django 5.1.4 on 2024-12-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orientacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientacao',
            name='solicitacaoAceita',
            field=models.BooleanField(default=False),
        ),
    ]
