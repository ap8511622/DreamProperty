# Generated by Django 3.0 on 2021-12-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_location',
            field=models.CharField(choices=[('Maninagar', 'Maninagar'), ('Memnagar', 'Memnagar'), ('Bopal', 'Bopal'), ('Iskon', 'Iskon')], default='Bopal', max_length=100),
        ),
    ]
