# Generated by Django 5.0.6 on 2024-07-12 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_monitoredsite_check_interval"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monitoredsite",
            name="check_interval",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
