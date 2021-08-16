# Generated by Django 3.2.6 on 2021-08-16 14:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0002_auto_20210815_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='boss',
            field=models.CharField(choices=[('비아키스', '비아키스'), ('발탄', '발탄'), ('쿠크세이튼', '쿠크세이튼'), ('아르고스', '아르고스')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='guide',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='mode',
            field=models.CharField(choices=[('노말', '노말'), ('하드', '하드'), ('헬', '헬'), ('리허설', '리허설'), ('어비스', '어비스')], default='노말', max_length=10),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='phase',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default='1', max_length=2),
        ),
    ]
