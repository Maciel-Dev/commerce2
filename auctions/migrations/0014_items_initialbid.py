# Generated by Django 3.2.3 on 2021-10-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_remove_items_initialbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='initialBid',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
