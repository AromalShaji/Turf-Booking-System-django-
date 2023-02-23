from django.contrib import admin
from  .models import Tournament_Booking,Turf_Booking,rating
# Register your models here.


admin.site.register(Tournament_Booking)
admin.site.register(Turf_Booking)
admin.site.register(rating)