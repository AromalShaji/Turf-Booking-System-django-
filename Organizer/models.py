from email.policy import default
from django.db import models
from Admin.models import Registration

# Create your models here.

class Turfregistration(models.Model):
    uid=models.CharField(max_length=100,  default='')
    turf_name = models.CharField(max_length=100)
    turf_location =  models.CharField(max_length=50,  default='')
    turf_address =  models.CharField(max_length=50,  default='')
    turf_desc = models.CharField(max_length=1000,  default='')
    turf_feature = models.CharField(max_length=50,  default='')
    turf_rate = models.CharField(max_length=50,  default='')
    turf_img = models.ImageField(upload_to='images',  default='')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.turf_name

class Host_Tournament(models.Model):
    uid=models.CharField(max_length=100, default='')
    Tournament_name = models.CharField(max_length=100)
    Tournament_date = models.CharField(max_length=20, default='')
    Tournament_desc = models.CharField(max_length=750, default='')
    Tournament_rate = models.CharField(max_length=50, default='')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.Tournament_name
