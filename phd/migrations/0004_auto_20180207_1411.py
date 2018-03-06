# Generated by Django 2.0.2 on 2018-02-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phd', '0003_auto_20180207_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='original_language',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='original_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
