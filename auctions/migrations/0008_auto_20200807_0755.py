# Generated by Django 3.0.9 on 2020-08-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_lot_max_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='max_bid',
            field=models.FloatField(),
        ),
    ]
