# Generated by Django 3.0.3 on 2020-07-02 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_adminstorage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminprofile',
            name='password',
        ),
    ]
