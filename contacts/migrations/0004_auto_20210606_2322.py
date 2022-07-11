# Generated by Django 3.2.3 on 2021-06-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20210606_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contact_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]
