# Generated by Django 3.0.8 on 2020-07-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200711_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='item_category',
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]