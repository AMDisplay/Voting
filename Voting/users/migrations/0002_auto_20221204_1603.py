# Generated by Django 3.1 on 2022-12-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_card',
            field=models.IntegerField(unique=True),
        ),
    ]
