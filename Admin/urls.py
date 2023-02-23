from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns=[
    path('', index,name='index'),
    path('about/<id>', about,name='about'),
    path('turf_reg/<id>', include('Organizer.urls'),name='turf_reg'),
    path('reg/',reg,name='reg'),
    path('login/', login,name='login'),
    path('lgout/', lgout,name='lgout'),
    path('tournament_about/<id>',tournament_about,name='tournament_about'),
    path('profile/', profile,name='profile'),
    path('search/', search,name='search'),
    path('cancel/<id>',cancel,name='cancel'),
    ]