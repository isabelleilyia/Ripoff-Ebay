# Generated by Django 3.0.8 on 2020-07-11 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_listing_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='item_category',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auctions.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
