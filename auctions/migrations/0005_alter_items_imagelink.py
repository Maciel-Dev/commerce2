# Generated by Django 3.2.3 on 2021-10-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_items_imagelink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='imageLink',
            field=models.ImageField(max_length=256, upload_to=''),
        ),
    ]