from django.urls import path
from .views import *

urlpatterns = [
    path('turf_reg/<id>',turf_reg,name='turf_reg'),
    path('tournament_reg/<id>',tournament_reg,name='tournament_reg'),
    ]