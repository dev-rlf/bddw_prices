# Generated by Django 3.2.12 on 2022-07-05 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("price_records", "0010_formulapricelistpricerecord_rule_display_2"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="formulapricelistpricerecord",
            options={"ordering": ["list_price"]},
        ),
        migrations.AlterModelOptions(
            name="formulapricerecord",
            options={"ordering": ["list_price"]},
        ),
        migrations.AlterModelOptions(
            name="pricelistpricerecord",
            options={"ordering": ["list_price"]},
        ),
    ]
