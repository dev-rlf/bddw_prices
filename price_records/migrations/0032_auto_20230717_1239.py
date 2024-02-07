# Generated by Django 3.2.12 on 2023-07-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_records', '0031_auto_20230712_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulapricelistpricerecord',
            name='gbp_price',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formulapricelistpricerecord',
            name='gbp_price_no_vat',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formulapricelistpricerecord',
            name='gbp_trade',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formulapricelistpricerecord',
            name='gbp_trade_no_vat',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]