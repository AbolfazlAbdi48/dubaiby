# Generated by Django 5.1.4 on 2025-04-28 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("travel", "0032_tour_currency"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hotel",
            name="ai_summary",
        ),
        migrations.RemoveField(
            model_name="tour",
            name="accommodation",
        ),
        migrations.RemoveField(
            model_name="tour",
            name="ai_summary",
        ),
        migrations.RemoveField(
            model_name="tour",
            name="transport_text",
        ),
        migrations.RemoveField(
            model_name="tour",
            name="transport_ticket",
        ),
    ]
