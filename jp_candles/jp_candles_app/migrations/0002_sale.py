# Generated by Django 4.0.2 on 2022-04-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jp_candles_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=128)),
                ('jp_candles', models.BooleanField()),
            ],
        ),
    ]
