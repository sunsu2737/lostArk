# Generated by Django 3.2.6 on 2021-08-16 16:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0005_alter_pattern_guide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='guide',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
