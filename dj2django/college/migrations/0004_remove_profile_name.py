# Generated by Django 3.0.6 on 2020-05-21 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
