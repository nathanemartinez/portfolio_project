# Generated by Django 3.0.2 on 2020-01-23 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='slug',
        ),
    ]
