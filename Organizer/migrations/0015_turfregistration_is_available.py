# Generated by Django 4.1.1 on 2022-12-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0014_alter_host_tournament_tournament_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfregistration',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
