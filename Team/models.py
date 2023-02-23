from email.policy import default
from django.db import models

# Create your models here.

class Tournament_Booking(models.Model):
    uid = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=100, default='')
    tid = models.CharField(max_length=100)
    Tournament_name= models.CharField(max_length=100, default='')
    turf_id = models.CharField(max_length=100, default='')

    def __str__(self)  -> str:
        return str(self.Tournament_name)+" : "+str(self.user_name)

class Turf_Booking(models.Model):
    uid = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=100, default='')
    Turf_name = models.CharField(max_length=100, default='')
    turf_id = models.CharField(max_length=100, default='')
    date = models.CharField(max_length=100, default='')
    start_time = models.CharField(max_length=100, default='')
    end_time = models.CharField(max_length=100, default='')
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.start_time) +" : "+ str(self.Turf_name)

class rating(models.Model):
    uid = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=100, default='')
    Turf_name = models.CharField(max_length=100, default='')
    turf_id = models.CharField(max_length=100, default='')
    star = models.CharField(max_length=100, default='')

    def __str__(self) -> str:
        return str(self.user_name) +" : "+ str(self.Turf_name)

