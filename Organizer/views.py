from django.shortcuts import render,redirect
from Admin.models import Registration
from django.http import HttpResponse
from .models import Turfregistration,Host_Tournament
from hashlib import sha256
from django.views.decorators.cache import cache_control
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import datetime

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def turf_reg(request,id):
    reg_turf = Turfregistration.objects.all()
    reg_tournament=Host_Tournament.objects.all() 
    dis = Registration.objects.get(id=id)
    user=dis.id
    userid = request.session['id']
    if request.method=='POST':
        turfname=request.POST.get('turfname')
        location=request.POST.get('location')
        address=request.POST.get('address')
        description=request.POST.get('description')
        features=request.POST.get('feat') 
        rate=request.POST.get('rate')
        img=request.FILES['image']
        ob=Turfregistration()
        ob.uid=userid
        ob.turf_name=turfname
        ob.turf_location=location
        ob.turf_address=address
        ob.turf_desc=description
        ob.turf_feature=features
        ob.turf_rate=rate
        ob.turf_img=img
        if(Turfregistration.objects.filter(uid=user)).exists():
            return HttpResponse('Turf already exist!!')
        if (Turfregistration.objects.filter(turf_name=turfname)).exists():
            return HttpResponse('Turf name already exist!!')
        ob.is_available=1
        ob.save()
        return redirect('index')
    else:
        return render(request,'turf_reg.html', {'id': userid,'dis':dis})

def tournament_reg(request,id):
    reg_turf = Turfregistration.objects.filter(is_available=1)
    reg_tournament=Host_Tournament.objects.filter(is_available=1)
    dis = Registration.objects.get(id=id)
    userid = request.session['id']
    today=datetime.datetime.now().strftime('%Y-%m-%d')
    if request.method=='POST':
        tournamentname=request.POST.get('tournamentname')
        tournamentdate=request.POST.get('tournamentdate')
        tournamentdescription=request.POST.get('tournamentdescription')
        tournamentrate=request.POST.get('tournamentrate')
        if(tournamentdate<today):
                return HttpResponse('Select an Upcoming Date')
        ob=Host_Tournament()
        ob.uid=userid
        ob.Tournament_name=tournamentname
        ob.Tournament_date=tournamentdate
        ob.Tournament_desc=tournamentdescription
        ob.Tournament_rate=tournamentrate
        if (Host_Tournament.objects.filter(Tournament_name=tournamentname)).exists():
            return HttpResponse('Tournament name already exist!!')
        ob.is_available=1
        ob.save()
        return render(request,'index.html', {'reg_turf': reg_turf,'id': userid,'dis':dis,'reg_tournament':reg_tournament})
    else:
        return render(request,'tournament_reg.html', {'id': userid,'dis':dis})


