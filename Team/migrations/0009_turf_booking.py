# Generated by Django 4.1.1 on 2022-12-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0008_tournament_booking_tournament_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turf_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=100)),
                ('user_name', models.CharField(default='', max_length=100)),
                ('tid', models.CharField(max_length=100)),
                ('Turf_name', models.CharField(default='', max_length=100)),
                ('turf_id', models.CharField(default='', max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
