# Generated by Django 3.0 on 2022-01-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_inquiry_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
