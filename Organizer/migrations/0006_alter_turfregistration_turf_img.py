# Generated by Django 4.1.1 on 2022-12-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0005_alter_turfregistration_turf_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turfregistration',
            name='turf_img',
            field=models.ImageField(upload_to='images'),
        ),
    ]