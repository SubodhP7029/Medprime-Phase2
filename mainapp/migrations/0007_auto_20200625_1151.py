# Generated by Django 3.0.3 on 2020-06-25 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200625_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminprofile',
            name='adminaddeddate',
        ),
        migrations.RemoveField(
            model_name='adminprofile',
            name='user',
        ),
    ]
