# Generated by Django 3.0.2 on 2020-02-02 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteChecker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.URLField()),
                ('scan', models.CharField(choices=[('Hourly', 'HOURLY'), ('Daily', 'DAILY'), ('Weekly', 'WEEKLY')], max_length=6)),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
        ),
    ]
