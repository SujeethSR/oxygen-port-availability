# Generated by Django 3.2.3 on 2021-06-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_hospital_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='Phone_No',
            field=models.CharField(blank=True, default='Phone No.', max_length=20),
        ),
    ]
