# Generated by Django 3.0.8 on 2020-07-11 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20200711_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='item_category',
        ),
    ]
