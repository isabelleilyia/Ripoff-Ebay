# Generated by Django 3.0.8 on 2020-07-10 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200710_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='item_category',
        ),
    ]
