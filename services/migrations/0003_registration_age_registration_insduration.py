# Generated by Django 4.1 on 2022-08-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_registration_delete_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registration',
            name='InsDuration',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
