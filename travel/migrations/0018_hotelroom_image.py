# Generated by Django 5.1.4 on 2025-01-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel", "0017_hotel_ai_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotelroom",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="hotels/", verbose_name="تصویر کاور"
            ),
        ),
    ]
