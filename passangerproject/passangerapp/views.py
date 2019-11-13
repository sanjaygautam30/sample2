from django.shortcuts import render
from .forms import CreatePassangerForm,DeletePassangerForm
from .models import Passanger

def getIndexPage(request):
    return render(request,'index.html')

def Addpassanger(request):
    cpf=CreatePassangerForm()
    return render(request,'add.html',{'form':cpf})

def savePassanger(request):
    pid=int(request.POST['pid'])
    fname=request.POST['fname']
    lname=request.POST['lname']
    age=int(request.POST['age'])
    seatno=int(request.POST['seatno'])
    p=Passanger(pid=pid, fname=fname, lname=lname, age=age, seatno=seatno)
    p.save()
    return render(request,'sucess.html')

def getdeletepage(request):
    dpf=DeletePassangerForm()
    return render(request,'delete.html',{'form':dpf})

def deletepassanger(request):
    pid=int(request.POST['pid'])
    p=Passanger(pid=pid) 
    p.delete()
    return render(request,'sucess.html')

def showpassanger(request):
    qs=Passanger.objects.all()
    return render(request,'show.html',{'passangers':qs})
