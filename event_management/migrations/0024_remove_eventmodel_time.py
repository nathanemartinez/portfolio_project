# Generated by Django 3.0.2 on 2020-01-31 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0023_eventmodel_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='time',
        ),
    ]
