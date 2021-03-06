# Generated by Django 3.0.8 on 2020-07-10 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200709_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='items',
        ),
        migrations.AlterField(
            model_name='listing',
            name='current_price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='item_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auctions.Category'),
        ),
    ]
