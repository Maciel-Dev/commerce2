# Generated by Django 3.2.3 on 2021-10-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_items_initialbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='initialBid',
            field=models.FloatField(null=True),
        ),
    ]