from django.shortcuts import render, redirect
from django.http import HttpResponse
from Admin.models import Registration
from Organizer.models import Turfregistration,Host_Tournament
from .models import Tournament_Booking,Turf_Booking,rating
from hashlib import sha256
from django.views.decorators.cache import cache_control
from django.db.models import Q
from django.contrib import messages
import datetime

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def tournament_booking(request,id):
    Tournament_details=Host_Tournament.objects.get(id=id)
    m=Tournament_details.uid
    user_id = request.session['id']
    dis = Registration.objects.get(id=user_id)
    reg=Turfregistration.objects.get(uid=m)
    if request.method=='POST':
        ob=Tournament_Booking()
        ob.uid=user_id
        ob.user_name=dis
        ob.tid=Tournament_details.id
        ob.Tournament_name=Tournament_details
        ob.turf_id=reg.id
        if (Tournament_Booking.objects.filter(uid=dis.id,tid=Tournament_details.id)).exists():
            return HttpResponse('Already Booked For This Tournament')
        else:
            ob.save()
            return HttpResponse('Tournament Booked')
    else:
        return HttpResponse('Something went wrong!...')

def turf_booking_details(request,id):
    turf_details=Turfregistration.objects.get(id=id)
    if 'id' in request.session:
        user_id = request.session['id']
        dis = Registration.objects.get(id=user_id)
        time_slot = Turf_Booking.objects.filter()
        return render(request,'turf_book.html', {'id': user_id,'dis':dis,'turf_details':turf_details,'time_slot':time_slot})
    else:
        return HttpResponse('You need to login to Book!')

def turf_booking(request,id):
    turf_details = Turfregistration.objects.get(id=id)
    turfid=turf_details.id
    if 'id' in request.session:
        user_id = request.session['id']
        dis = Registration.objects.get(id=user_id)
        if request.method == 'POST':
            ob=Turf_Booking()
            st = request.POST.get('start_time')
            et = request.POST.get('end_time')
            dt = request.POST.get('turf_date')
            today=datetime.datetime.now().strftime('%Y-%m-%d')
            if(st==''):
                return HttpResponse('All Field need to Fill!')
            elif(et==''):
                return HttpResponse('All Field need to Fill!')
            elif(dt==''):
                return HttpResponse('All Field need to Fill!')
            elif(dt<today):
                return HttpResponse('Select another date')
            ob.uid=user_id
            ob.user_name=dis
            ob.Turf_name=turf_details
            ob.turf_id=turf_details.id
            if(Turf_Booking.objects.filter(date=dt,start_time=st, end_time=et,turf_id=turfid)).exists():
                return HttpResponse('Time is not available')
            ob.date=dt
            ob.start_time=st
            ob.end_time=et
            ob.is_available=1
            ob.save()
            return HttpResponse('Turf is Booked')
    else:
        return HttpResponse('Need To Login')

def rate(request,id):
    turf_details = Turfregistration.objects.get(id=id)
    turfid=turf_details.id
    if 'id' in request.session:
        user_id = request.session['id']
        dis = Registration.objects.get(id=user_id)
        if request.method == 'POST':
            ob=rating()
            star = request.POST.get('rate')
            ob.uid=user_id
            ob.user_name=dis
            ob.Turf_name=turf_details.turf_name
            ob.turf_id=turf_details.id
            ob.star=star
            if(rating.objects.filter(uid=user_id,turf_id=turf_details.id)).exists():
                rating.objects.filter(uid=user_id,turf_id=turf_details.id).update(star=star)
                return HttpResponse('Rating updated')
            ob.save()
            return HttpResponse('Rating given')
        return redirect('about')