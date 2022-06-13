# Generated by Django 3.2.12 on 2022-06-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_catseriesitem_formula_tear_sheet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='catseriesitem',
            options={'verbose_name': 'Category Series Item', 'verbose_name_plural': 'Category Series Items'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='order',
        ),
        migrations.RemoveField(
            model_name='catseriesitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='series',
            name='order',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
