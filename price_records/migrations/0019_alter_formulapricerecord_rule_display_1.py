# Generated by Django 3.2.12 on 2022-07-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("price_records", "0018_auto_20220719_1010"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulapricerecord",
            name="rule_display_1",
            field=models.CharField(
                blank=True,
                help_text="Will convert [LENGTH] L x [DEPTH] D or you can just manually ",
                max_length=200,
                null=True,
            ),
        ),
    ]
