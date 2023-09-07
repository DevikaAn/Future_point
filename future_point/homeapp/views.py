from django.shortcuts import render
from django.http import HttpResponse
from . models import User_tb3_nw
# Create your views here.
def reg(request):
    if request.method=="POST":
        a = request.POST.get("studentname")
        b= request.POST.get("address")
        c= request.POST.get("phoneno")
        d = request.POST.get("dob")
        e = request.POST.get("gname")
        f = request.POST.get("username")
        g = request.POST.get("passwd")
        h = request.POST.get("email")
        i = request.POST.get("gender")
        k = request.POST.get("gphno")


        obj=User_tb3_nw.objects.create(studentname=a,address=b,phoneno=c,dob=d,gname=e,username=f,passwd=g,
        email=h,gender=i,gphno=k)
        obj.save()
        if obj:
            l = "successfully registered"
            return render(request, 'studreg.html', {"success": l})
        else:
            l = " not successfully registered"
            return render(request, 'studreg.html', {"success": l})

    else :
            return render(request,'studreg.html')

def streg(request):
    return render(request,'index.html')
def vi(request):
    viobj=User_tb3_nw.objects.all()
    return render(request,'showdetail.html',{'data':viobj})
def foodlogin(request):
    return render(request,'fudlogin.html')
def index(request):
    return render(request,'home/index.html')