# Generated by Django 3.2.3 on 2021-10-20 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_alter_items_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='imageLink',
            field=models.CharField(max_length=512),
        ),
    ]
