# Generated by Django 4.0.2 on 2022-04-24 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jp_candles_app', '0004_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='quantity',
            new_name='quantity_of_product',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='sale',
            new_name='sales_channel',
        ),
    ]
