# Generated by Django 3.0.8 on 2020-07-09 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='item_category',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing')),
            ],
        ),
    ]