# Generated by Django 5.1.4 on 2024-12-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInteresse',
            fields=[
                ('area_interesse_ID', models.AutoField(primary_key=True, serialize=False)),
                ('area_interesse_nome', models.CharField(max_length=150)),
            ],
        ),
    ]
