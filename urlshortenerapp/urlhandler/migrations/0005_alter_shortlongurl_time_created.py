# Generated by Django 3.2.9 on 2021-11-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlhandler', '0004_alter_shortlongurl_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlongurl',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
