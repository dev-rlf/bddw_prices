# Generated by Django 3.2.12 on 2023-07-12 17:35

from django.db import migrations, models
import tear_sheets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tear_sheets', '0010_alter_tearsheet_gbp_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tearsheet',
            name='sdata',
            field=models.JSONField(blank=True, default=tear_sheets.models.TearSheet.json_default, null=True),
        ),
    ]