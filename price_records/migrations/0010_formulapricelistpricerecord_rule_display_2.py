# Generated by Django 3.2.12 on 2022-06-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("price_records", "0009_auto_20220628_0933"),
    ]

    operations = [
        migrations.AddField(
            model_name="formulapricelistpricerecord",
            name="rule_display_2",
            field=models.CharField(
                blank=True,
                default=" ",
                help_text="ex. / 2 STANDARD DRAWERS / 2 CABS",
                max_length=200,
                null=True,
            ),
        ),
    ]
