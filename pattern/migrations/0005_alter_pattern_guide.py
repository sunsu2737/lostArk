# Generated by Django 3.2.6 on 2021-08-16 16:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0004_alter_pattern_guide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='guide',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
