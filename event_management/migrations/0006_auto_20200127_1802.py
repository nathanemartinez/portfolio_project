# Generated by Django 3.0.2 on 2020-01-28 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0005_guestmodel_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestmodel',
            name='token',
            field=models.CharField(blank=True, default='7bf868e88fd048de83badfcfe0f78d16', max_length=100, null=True),
        ),
    ]
