# Generated by Django 3.0.3 on 2020-07-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_adminprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='testallowed',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
