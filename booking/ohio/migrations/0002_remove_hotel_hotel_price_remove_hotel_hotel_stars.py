# Generated by Django 5.1.4 on 2025-01-06 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ohio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='hotel_price',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='hotel_stars',
        ),
    ]
