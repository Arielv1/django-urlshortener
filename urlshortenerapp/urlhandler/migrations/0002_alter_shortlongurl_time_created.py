# Generated by Django 3.2.9 on 2021-11-14 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlhandler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlongurl',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 14, 22, 8, 56, 749285)),
        ),
    ]
