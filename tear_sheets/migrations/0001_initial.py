# Generated by Django 3.2.12 on 2022-06-07 12:42

from django.db import migrations, models
import django.db.models.deletion
import tear_sheets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TearSheet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        default=None,
                        help_text="This will appear at the top of the tearsheet.",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default_image.jpg",
                        help_text="Usually the collage jpg containing dif items.",
                        null=True,
                        upload_to=tear_sheets.models.image_upload_to,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TearSheetFooterDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, default="", max_length=1000, null=True
                    ),
                ),
                ("details", models.CharField(max_length=1000)),
                (
                    "order",
                    models.IntegerField(
                        help_text="The order number when this record appears with like records."
                    ),
                ),
                (
                    "tear_sheet",
                    models.ForeignKey(
                        help_text="Details must be attached to a tearsheet.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tear_sheets.tearsheet",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TearSheetDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, default="", max_length=1000, null=True
                    ),
                ),
                ("details", models.CharField(max_length=1000)),
                (
                    "order",
                    models.IntegerField(
                        help_text="The order number when this record appears with like records."
                    ),
                ),
                (
                    "tear_sheet",
                    models.ForeignKey(
                        help_text="Details must be attached to a tearsheet.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tear_sheets.tearsheet",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ImageCaption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_no",
                    models.IntegerField(
                        help_text="The order number when this record appears with like records."
                    ),
                ),
                (
                    "caption_title",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Usually the position of the image being described.",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="The image caption. Usually a product description.",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "tear_sheet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tear_sheets.tearsheet",
                    ),
                ),
            ],
            options={
                "ordering": ["order_no"],
            },
        ),
    ]
