# Generated by Django 3.2.4 on 2021-08-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210817_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='slot_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='slot',
            name='slot_2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
