# Generated by Django 3.2.12 on 2022-06-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_catseriesitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='catseriesitem',
            name='opt_series_item_display',
            field=models.CharField(blank=True, default=None, help_text='The string version of the formula', max_length=200, null=True),
        ),
    ]
