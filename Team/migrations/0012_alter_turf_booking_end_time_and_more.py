# Generated by Django 4.1.1 on 2022-12-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0011_remove_turf_booking_tid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf_booking',
            name='end_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='turf_booking',
            name='start_time',
            field=models.CharField(default='', max_length=100),
        ),
    ]