# Generated by Django 2.1.1 on 2018-09-22 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0011_auto_20180922_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qoute',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
