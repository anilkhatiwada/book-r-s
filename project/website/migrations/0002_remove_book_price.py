# Generated by Django 4.0.6 on 2022-08-01 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
    ]
