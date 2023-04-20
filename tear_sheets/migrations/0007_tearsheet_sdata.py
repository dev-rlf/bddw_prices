# Generated by Django 3.2.12 on 2023-04-12 19:09

from django.db import migrations, models
import tear_sheets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tear_sheets', '0006_alter_tearsheet_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='tearsheet',
            name='sdata',
            field=models.JSONField(blank=True, default=tear_sheets.models.TearSheet.json_default, null=True),
        ),
    ]
