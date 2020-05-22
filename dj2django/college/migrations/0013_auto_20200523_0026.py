# Generated by Django 3.0.6 on 2020-05-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0012_auto_20200523_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='my_img',
        ),
        migrations.AddField(
            model_name='profile',
            name='myimg',
            field=models.ImageField(blank=True, null=True, upload_to='images\\'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='myresume',
            field=models.FileField(blank=True, null=True, upload_to='docs\\'),
        ),
    ]
