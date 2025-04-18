# Generated by Django 5.1.4 on 2025-01-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel", "0018_hotelroom_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="location_img",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="hotels/loc/",
                verbose_name="تصویر لوکیشن",
            ),
        ),
    ]
