# Generated by Django 5.0.6 on 2024-07-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_monitoredsite_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoredsite',
            name='keyword',
            field=models.CharField(max_length=100),
        ),
    ]