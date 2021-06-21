from django.shortcuts import render
from django.http import HttpResponse
from .models import users, govt
import hashlib
import json
# Create your views here.
salt_user="f1nd1ngn3m0"
salt_govt="h311oW0rID"

def index(request):
    return render(request,'taxcalculate/wbst.html')

def index_submit(request):
    if request.method=='POST':
        uid=request.POST.get('uid')
        uid_1=hashlib.sha256((uid+salt_user).encode()).hexdigest()
        name=request.POST.get('name')
        name_1=hashlib.sha256((name+salt_user).encode()).hexdigest()
        q=users.objects.filter(uid=uid_1)
        if q.exists():
            if q[0].name==name_1:
                return HttpResponse(json.dumps({'error':0,'info':'The user is verified'}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'error':1,'info':'The user is not verified'}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'error':1,'info':'The user doesn\'t exist'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}), content_type="application/json")

def createNewUser(request):
    return render(request,'taxcalculate/regis.html')

def createNewUser_submit(request):
    if request.method == 'POST':
        uid=request.POST.get('uid')
        uid_1=hashlib.sha256((uid+salt_user).encode()).hexdigest()
        uid_2=hashlib.sha256((uid+salt_govt).encode()).hexdigest()
        name=request.POST.get('name')
        name_1=hashlib.sha256((name+salt_user).encode()).hexdigest()
        name_2=hashlib.sha256((name+salt_govt).encode()).hexdigest()
        address=request.POST.get('add')
        ph_no=request.POST.get('phno')
        tax_amt=request.POST.get('taxamt')
        if users.objects.filter(uid=uid_1).exists():
            return HttpResponse(json.dumps({'error':1,'info':'The user already exists'}), content_type="application/json")
        else:
            q1=users(uid=uid_1,name=name_1)
            q1.save()
            q2=govt(uid=uid_2,name=name_2,address=address,ph_no=ph_no,tax_amt=tax_amt)
            q2.save()
            return HttpResponse(json.dumps({'error':0,'info':'The user has been created'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}), content_type="application/json")

def login(request):
    if request.method =='POST':
        uid=request.POST.get('uid')
        uid_1=hashlib.sha256((uid+salt_govt).encode()).hexdigest()
        name=request.POST.get('name')
        name_1=hashlib.sha256((name+salt_govt).encode()).hexdigest()
        q=govt.objects.filter(uid=uid_1)
        if q.exists():
            address=q[0].address
            ph_no=q[0].ph_no
            tax_amt=q[0].tax_amt
            return render(request,'taxcalculate/login.html',{'tax_amt':tax_amt,'ph_no':ph_no,'address':address,'uid':uid,'name':name})
        return HttpResponse('User Credentials is not correct')
    else:
        return HttpResponse('User Have Not Logged In Please Go Back')


