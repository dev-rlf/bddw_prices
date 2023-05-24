# Generated by Django 3.2.12 on 2023-05-08 15:18

from django.db import migrations, models
import formula_tear_sheets.models


class Migration(migrations.Migration):
    dependencies = [
        ("formula_tear_sheets", "0004_formulatearsheet_template"),
    ]

    operations = [
        migrations.AddField(
            model_name="formulatearsheet",
            name="sdata",
            field=models.JSONField(
                blank=True, default=formula_tear_sheets.models.json_default, null=True
            ),
        ),
    ]
