# Generated by Django 3.0.2 on 2020-01-28 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0007_auto_20200127_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestmodel',
            name='token',
            field=models.CharField(blank=True, default='26467ab06c034a07ad2a7490cdd76bf5', max_length=100, null=True, unique=True),
        ),
    ]
