# Generated by Django 5.0.6 on 2024-06-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoredSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('check_interval', models.IntegerField(help_text='Interval in minutes')),
                ('search_phrase', models.CharField(blank=True, max_length=255, null=True)),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('last_changed', models.DateTimeField(blank=True, null=True)),
                ('phrase_found', models.BooleanField(default=False)),
            ],
        ),
    ]
