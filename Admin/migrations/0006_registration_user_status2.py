# Generated by Django 4.1.1 on 2023-02-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_alter_registration_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='user_status2',
            field=models.IntegerField(default='1'),
        ),
    ]