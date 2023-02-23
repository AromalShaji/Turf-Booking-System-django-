from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('tournament_booking/<id>',tournament_booking,name='tournament_booking'),
    path('turf_booking_details/<id>',turf_booking_details,name='turf_booking_details'),
    path('turf_booking/<id>',turf_booking,name='turf_booking'),
    path('rate/<id>',rate,name='rate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)