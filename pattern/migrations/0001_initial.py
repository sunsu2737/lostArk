# Generated by Django 3.2.6 on 2021-08-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss_name', models.TextField(default='', max_length=20)),
                ('mode', models.TextField(default='', max_length=20)),
                ('phase', models.TextField(default='1', max_length=1)),
                ('guide', models.TextField(default='공략없음', max_length=1000, null=True)),
            ],
        ),
    ]