# Generated by Django 3.2.20 on 2023-07-23 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fourth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='reservervation_id',
        ),
    ]
