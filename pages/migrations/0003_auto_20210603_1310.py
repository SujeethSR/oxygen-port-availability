# Generated by Django 3.2.3 on 2021-06-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210601_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='district',
            field=models.CharField(blank=True, default='District', max_length=100),
        ),
        migrations.AddField(
            model_name='hospital',
            name='state',
            field=models.CharField(blank=True, default='State', max_length=100),
        ),
    ]
