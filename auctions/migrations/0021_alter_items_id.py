# Generated by Django 3.2.3 on 2021-10-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_alter_items_initialbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]