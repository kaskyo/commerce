# Generated by Django 3.0.9 on 2020-08-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200806_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='last_bump',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
