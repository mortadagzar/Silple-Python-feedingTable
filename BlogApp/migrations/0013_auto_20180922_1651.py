# Generated by Django 2.1.1 on 2018-09-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0012_auto_20180922_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qoute',
            name='image',
        ),
        migrations.AddField(
            model_name='qoute',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
