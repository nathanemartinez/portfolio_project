# Generated by Django 3.0.2 on 2020-03-04 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0026_auto_20200203_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 4, 13, 1, 45, 782312), null=True),
        ),
    ]
