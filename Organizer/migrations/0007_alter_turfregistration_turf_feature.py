# Generated by Django 4.1.1 on 2022-12-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0006_alter_turfregistration_turf_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turfregistration',
            name='turf_feature',
            field=models.CharField(default='', max_length=50),
        ),
    ]
