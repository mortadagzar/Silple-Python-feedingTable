# Generated by Django 2.1.1 on 2018-09-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_auto_20180922_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoute',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
