# Generated by Django 3.0.3 on 2020-06-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20200627_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminstorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatorid', models.IntegerField(blank=True, null=True)),
                ('deletorid', models.IntegerField(blank=True, null=True)),
                ('typeofchange', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
