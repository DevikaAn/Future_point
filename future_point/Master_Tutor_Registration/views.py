from django.shortcuts import render,redirect
from django.http import HttpResponse
from tutorapp.models import tutorReg_tbl
from Minor_Programmer.models import User_mp
from . models import User_mtr
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import random
from django.conf import settings
from django.core.mail import send_mail
from admin_module.models import course
# MatPlotLib
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

def password_gen():
    sp=['@','#','$','%','&','*',')']
    
    print(ord('A'),ord('Z'),ord('a'),ord('z'))
    
    codeno=""

    for i in range(0,2):
        j=random.randint(0,6)
        
        codeno=codeno+chr(random.randrange(65,90))+sp[j]+str(random.randint(0,9))
    return codeno       

def matuemail(request):
    if request.method=="POST":

        subject=request.POST.get("subjectmt")
        msg=request.POST.get("messagemt")
        to=request.POST.get("tomt")
        res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
        if(res==1):
            msg="mail send successfully"
            return render(request, 'mtemail.html', {'msg': msg})
        else:
            msg="mail could not send"
            return render(request, 'mtemail.html', {'msg': msg})
    else:
        msg=" "
        return render(request,'mtemail.html',{'msg':msg})

# Create your views here.
def home(request):
    piechart()
    crs=course.objects.all()
    user=request.session['username']
    password=request.session['password']
    
    obj=User_mtr.objects.filter(email=user,passwd=password)
    return render(request,'master_homepage.html',{'course':crs,'mast':obj})
def matureg(request):
    if request.method=="POST":
        a = request.POST.get("mtname")
        b= request.POST.get("address")
        c= request.POST.get("phoneno")

        #e=request.POST.get("dpt")
        # f = request.POST.get("username")
        # g = request.POST.get("passwd")
        h = request.POST.get("email")
        i = request.POST.get("gender")
       # j=request.POST.get("desi")
        #rno = random.randrange(499, 699)
        #rno = str(rno)
        #passw = a[0:3] + rno
        passwd = password_gen()


        ph=len(c)   
        ph=int(ph)
        if ph==10:

            obj=User_mtr.objects.create(mtname=a,address=b,phoneno=c,dpt="dpt",username=h,passwd=passwd,
            email=h,gender=i,desi="desi")
            obj.save()
            if obj:
                subject = "Username and Password"
                msg = "Your Username:" + h + "\n Password:" + passwd + "\n Login using this link http://127.0.0.1:8000/Master_Tutor_Registration/login"
                to = h
                res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
                if res:
                    l = "successfully registered  mail send"
                else:
                    l = "registered  successfully mail not send"

                return render(request, 'Master_tut_reg.html', {"success": l})
            else:
                # l = " not successfully registered"
                return render(request, 'Master_tut_reg.html', {"success": "not successfully"})

        else:
                return  render(request,'Master_tut_reg.html',{"success":"check your Phone Number"})     

    else :
            return render(request,'Master_tut_reg.html')

def mtv(request):
    mtrobj=User_mtr.objects.all()
    return render(request,'mastertutordetails.html',{'data':mtrobj})
# Pie Chart



def piechart():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Tutor', 'MProgrammer'
    totr=tutorReg_tbl.objects.all().count()
    mpr=User_mp.objects.all().count()
    sizes = [totr, mpr]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('Assets/Mst.png',dpi=100)
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("passw")
        obj=User_mtr.objects.filter(email=username,passwd=password)
        if obj:
            request.session['username']=username
            request.session['password']=password
            dataset=User_mtr.objects.all()
            crs=course.objects.all()
            return render(request,'master_homepage.html',{'data':obj,'dataset':dataset,'course':crs})
        else:
            request.session['username']=""
            request.session['password']=""
            return render(request,'MasterLogin.html',{'lmsg':"incorrect username or password"})
    else:
        msg=" "
        return render(request,'MasterLogin.html',{'lmsg':msg})
def delt(request):
    idno=request.GET.get("idn")
    mast=User_mtr.objects.get(id=idno)
    mast.delete()
    return redirect("/admin_module/home")