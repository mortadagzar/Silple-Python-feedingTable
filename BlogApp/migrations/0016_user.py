# Generated by Django 2.1.1 on 2018-09-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0015_auto_20180922_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('email', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
