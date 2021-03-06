# Generated by Django 3.0.9 on 2020-08-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_lot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='lenght',
            new_name='length',
        ),
        migrations.AlterField(
            model_name='bid',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
