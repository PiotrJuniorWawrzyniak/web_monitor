# Generated by Django 5.0.6 on 2024-07-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_monitoredsite_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoredsite',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
