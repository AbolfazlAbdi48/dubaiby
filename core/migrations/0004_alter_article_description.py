# Generated by Django 5.1.4 on 2025-03-07 18:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_article_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                verbose_name="توضیحات"
            ),
        ),
    ]
