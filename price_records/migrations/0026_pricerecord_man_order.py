# Generated by Django 3.2.12 on 2022-12-28 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_records', '0025_auto_20221221_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricerecord',
            name='man_order',
            field=models.BooleanField(default=False),
        ),
    ]
