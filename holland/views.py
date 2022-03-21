from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .models import survey as su
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


def crops(request,name):
    info=Crop.objects.filter(name=name)
    print(info)
    return render(request,'crop.html',{'info':info})

    # return render(request,'dealerlogin.html')



    # de=dealer.objects.filter(pk=int(username))

    # return render(request,'dealerlogin.html',de)
def survey(request):
    if request.method=='POST' and len(request.POST['username'])>3:
        if len(request.POST['username'])>3:
            print('this line:-',request.POST['username'],request.POST['password'])
            print(request.POST['username']==11190 and request.POST['password']==123)
            if request.POST['username']=='11190' and request.POST['password']=='123':
                return render(request,'survey.html',{'username':request.POST['username'],'password':request.POST['password'],'name':'Amlesh Kumar'})
            else:
                return render(request,'login.html',{'error':'Please check userame and password'})

    if request.method=='POST':
        code=request.POST['emp_code']
        name=request.POST['farmer-name']
        namep=request.POST['farmer-parent']
        regd=request.POST['regd-no.']
        number=request.POST['farmer-number']
        system=request.POST['optionsdrip']
        spacing=request.POST['spacing']
        crop=request.POST['select-crop']
        pump=request.POST['pumpoption']
        area=request.POST['field-area']
        type=request.POST['surveyType']

        print({'code':code,'name':name,'namep':namep,'regd':regd,'number':number,'system':system,'spacing':spacing,'crop':crop,
        'pump':pump,'area':area,'type':type})
        data=su(code=code,name=name,namep=namep,regd=regd,number=number,system=system,spacing=spacing,crop=crop,pump=pump,area=area,type=type)
        print('data:',data)
        data.save()
        return render(request,'survey.html',{'username':request.POST['username'],'password':request.POST['password'],'name':'Amlesh Kumar','message':'Farmer Added Sucessfully'})

    return render(request,'login.html')


def about(request):
    return render(request,'aboutus.html')


def products(request):
    return render(request,'products.html')
