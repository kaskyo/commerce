# Generated by Django 3.0.9 on 2020-08-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_lot_last_bump'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='status',
            field=models.CharField(default='Open', max_length=64),
            preserve_default=False,
        ),
    ]