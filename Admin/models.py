from email.policy import default
from django.db import models

# Create your models here.

class Registration(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=20, default='')
    user_pass = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=12)
    user_status = models.IntegerField( default='1')
    role = models.CharField(max_length=100, default='team')

    def __str__(self):
        return self.user_name

