# Generated by Django 5.1.4 on 2025-01-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel", "0011_tour_ai_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="image_cover",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="tours/images",
                verbose_name="تصویر کاور",
            ),
        ),
    ]
