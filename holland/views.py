from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')


def dealer_auth(request):
    if request.method=='POST':
        username=request.POST['dealer_code']
        password=request.POST['dealer_password']
        dealer_info = {'dealer_info':dealer.objects.filter(pk=int(username)).first()}
        print(dealer_info)
        if dealer_info:
            if password==dealer_info['dealer_info'].dealer_password:
                print(dealer_info)
                return render(request,'dealer_info.html',dealer_info)
            else:
                return render(request,'dealerlogin.html',{'message':'wrong password! Please try again'})
        else:
            return render(request,'dealerlogin.html',{'message':'Dealer code does not exist please contact administrator'})

    return render(request,'dealerlogin.html')


def crops(request):
    info=Crop.objects.all()
    return render(request,'crop.html',{'info':info})

    # return render(request,'dealerlogin.html')



    # de=dealer.objects.filter(pk=int(username))

    # return render(request,'dealerlogin.html',de)



def about(request):
    return render(request,'aboutus.html')
