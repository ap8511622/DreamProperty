# Generated by Django 3.0 on 2022-01-03 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20220103_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='block',
        ),
        migrations.RemoveField(
            model_name='user',
            name='delete',
        ),
    ]
