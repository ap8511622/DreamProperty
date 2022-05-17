# Generated by Django 3.0 on 2021-11-16 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('Flat', 'Flat'), ('Tenament', 'Tenament')], max_length=100)),
                ('property_sub_type', models.CharField(choices=[('1 BHK', '1 BHK'), ('2 BHK', '2 BHK'), ('3 BHK', '3 BHK'), ('4 BHK', '4 BHK')], max_length=100)),
                ('property_area', models.CharField(max_length=100)),
                ('property_price', models.CharField(max_length=100)),
                ('property_address', models.TextField()),
                ('property_image1', models.ImageField(upload_to='images/')),
                ('property_image2', models.ImageField(upload_to='images/')),
                ('property_image3', models.ImageField(upload_to='images/')),
                ('property_image4', models.ImageField(upload_to='images/')),
                ('property_image5', models.ImageField(upload_to='images/')),
                ('property_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]
