import email
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import User_mp,Course 
from Master_Tutor_Registration.models import Notes_tbl,Works_tbl
from  Minor_Programmer.models import User_mp as mp
from Master_Tutor_Registration.models import minorwork_tbl
from admin_module.models import course
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import os
from django.http.response import Http404
import random
from  tutorapp.models import appre_tbl,tutorReg_tbl
from tutorapp.models import Sendlink
import  datetime
import string
def Notes(request):
            idn=request.GET.get("mpid")
            idno=request.session['stdid']
            # obj=mp.objects.filter(id=idno)
            obj=mp.objects.filter(id=idno) 
            for  c in obj:
                cr=c.mcs
            
            noobj = Notes_tbl.objects.filter(crs=cr)
            return render(request, 'notes.html', {'data': noobj})
def urllink(req):
    idn=req.session['mpid']
    print(idn)
    std=mp.objects.filter(id=idn)
    for l in std:
        v=l.batch
        lv=Sendlink.objects.filter(batch=v)
    return render(req,'liveclass.html',{'url':lv})  
def password_gen():
    sp=['@','#','$','%','&','*',')']
    
    print(ord('A'),ord('Z'),ord('a'),ord('z'))
    
    codeno=""

    for i in range(0,2):
        j=random.randint(0,6)
        
        codeno=codeno+chr(random.randrange(65,90))+sp[j]+str(random.randint(0,9))
    return codeno       

def mipremail(request):
    if request.method=="POST":

        subject=request.POST.get("subjectmp")
        msg=request.POST.get("messagemp")
        to=request.POST.get("tomp")
        res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
        if(res==1):
            msg="mail send successfully"
            return render(request, 'mpemail.html', {'msg': msg})
        else:
            msg="mail could not send"
            return render(request, 'mpemail.html', {'msg': msg})
    else:
        msg=" "
        return render(request,'mpemail.html',{'msg':msg})

# Create your views here.

def loginpage(request):
    return render(request,'MinorLogin.html')

# Create your views
def home(request):
    user=request.session['mpusername']
    passw=request.session['mppassword']
    if user==""and passw=="":
        return redirect("/Minor_Programmer/")
    else:
        obj=mp.objects.filter(email=user,passwd=passw)
        if obj:
            for ls in obj:
               
                stdid=ls.id
                crs_sel=ls.mcs
                btch=ls.batch
            request.session['stdid']=stdid


        # ap = appre_tbl.objects.filter(studentid=stdid)
            stdid=request.session['mpid']
            obj2=mp.objects.get(id=stdid)
            crs=course.objects.all()
            request.session['mpbatch']=btch
            ap=appre_tbl.objects.filter(studentid=obj2)
        if ap:
            for ls  in ap:
                appr=ls.appreciation

            if appr=="images/ribbon.png":
                s1=True
                s2=False
                s3=False
            elif appr=="images/badge.png":
                s1=False 
                s2=True
                s3=False
            elif appr=="images/best-seller.png":
                s1=False
                s2=False
                s3=True     
            stdn="Welcome, "+stdname
            crs="Your course :"+crs_sel
            return render(request,'minor_homepage.html',{'s1':s1,'s2':s2,'s3':s3,"course":crs,'selectcrs':crs_sel,'std':obj})
        else:
            return render(request,'minor_homepage.html',{'s1':False,'s2':False,'s3':False,"course":crs,'selectcrs':crs_sel,'std':obj})

def logout(request):
    request.session['username']=""
    request.session['password']=""
    return redirect("/Minor_Programmer/")
def mpreg(request):
    if request.method=="POST":
        a = request.POST.get("mpname")
        b= request.POST.get("address")
        c= request.POST.get("phoneno")
        d=request.POST.get("dob")
        # f = request.POST.get("username")
        # g = request.POST.get("passwd")
        h = request.POST.get("email")
        i = request.POST.get("gender")
        j=request.POST.get("gn")
        k=request.POST.get("gpn")
        p=request.POST.get("crs")
        q=request.POST.get("sname")
        lower = string.ascii_lowercase
        upper=string.ascii_uppercase
        num=string.digits
        symbols=string.punctuation
        all=lower+upper+num+symbols
        temp=random.sample(all,8)
        password="".join(temp)
        codeno=chr(random.randrange(97,104))+chr(random.randrange(0,128))+str(chr(random.randrange(200,600)))
        print(codeno)
       #print(password)
        #rno=random.randrange(499,699)
       # rno=str(rno)
       # passw=a[0:3]+rno
        passw=password_gen()

        obj=mp.objects.create(mpname=a,address=b,phoneno=c,dob=d,username=h,passwd=passw,email=h,gender=i,gn=j,gpn=k,vrf="not",mcs=p,sname=q)
        obj.save()
        if obj:
            l = "successfully registered  username and password will send to mail with in two days after the confirmation"

            obj2 = course.objects.all()
            return render(request, 'mp_Registration.html', {"success": l,'data':obj2})
        else:
            obj2 = course.objects.all()
            l = " not successfully registered"
            return render(request, 'mp_Registration.html', {"success": l,'data':obj2})

    else :
            obj2 = course.objects.all()
            return render(request,'mp_Registration.html' ,{'data':obj2})



def edt(request):
    if request.method=="POST":
        idno = request.POST.get("mpid")
        obj = User_mp.objects.filter(id=idno)
        adr=request.POST.get("addrs")
        ph=request.POST.get("ph")
        upd=User_mp.objects.get(id=idno)
        upd.address=adr
        upd.phoneno=ph
        upd.save()
        return redirect("/Minor_Programmer/view_mp")
    else:
        idno=request.session['mpid']
        obj=mp.objects.filter(id=idno)
        return render(request,'editminor.html',{'data':obj})    

def update(request):
        if request.method == "POST":
            a = request.POST.get("mpname")
            b = request.POST.get("address")
            c = request.POST.get("phoneno")
            e = request.POST.get("dob")
            f = request.POST.get("username")
            g = request.POST.get("passwd")
            h = request.POST.get("email")

            j = request.POST.get("gn")
            k= request.POST.get("gpn")
            p= request.POST.get("mcs")
            q= request.POST.get("sname")

            idno = request.POST.get("mpid")
            upobj = User_mp.objects.get(id=idno)
            upobj.mpname = a
            upobj.address = b
            upobj.phoneno = c
            upobj.dob = e
            upobj.username = f
            # upobj.passwd = g
            # upobj.email = h

            upobj.gn= j
            upobj.gpn=k
            # upobj.mcs=p
            # upobj.sname=q
            upobj.save()
            return redirect("/Minor_Programmer/home")
def  view_mp(request):

    user = request.session['mpusername']
    passw = request.session['mppassword']
    if user == "" and passw == "":
        return redirect("/Minor_Programmer/")
    obj=User_mp.objects.filter(username=user,passwd=passw)
    msg=""
    return render(request,'viewprofile.html',{'data':obj,'msg':msg})
    if request.method=="POST":
        user = request.session['username']
        passw = request.session['password']
        if user == "" and passw == "":
            return redirect("/Minor_Programmer/")
        else:
            obj2=User_mp.objects.filter(username=user,passwd=passw)
            for ls in obj2:
                idno=ls.id
            upd=User_mp.objects.filter(id=idno)
            upd.phoneno=request.POST.get("ph")
            upd.address=request.POST.get("addrs")
            upd.save()
            msg="updated"

            return render(request,'viewprofile.html',{'data':obj2,'msg':msg})


def index(request):
    return render(request,'index.html')

def onlineeditor(request):
    return render(request,'onlineeditor.html')


def mpegis(request):
    # mpobj=User_mp.objects.filter(vrf="not")
    frm = request.GET.get('frm')
    print(frm)
    if frm == 'MPADM':
        mpobj = User_mp.objects.filter(vrf="not")
        cfobj = User_mp.objects.filter(vrf="confirm")
        return render(request, 'mpadmin.html', {'data': mpobj,'confirm':cfobj})
    else:
        mpobj = User_mp.objects.filter(vrf="confirm")
        return render(request,'mp_details.html',{'data':mpobj})
def mpegisT(request):
    if request.GET.get("msg"):
        msg=request.GET.get("msg")
       
        mpobj = User_mp.objects.filter(vrf="confirm")
        return render(request, 'mpdetailT.html', {'data': mpobj,'msg':msg})
    tut=request.session['tutid']
    print("tutid",tut)
    tobj=tutorReg_tbl.objects.filter(id=tut)
    for l in tobj:
        crs=l.dpt
    print(crs)
    mpobj=User_mp.objects.filter(vrf="confirm",mcs=crs)
    return render(request,'mpdetailT.html',{'data':mpobj})

def minorwork(request):
        if request.method == "POST":
            assname= request.POST.get("an")
            assign= request.FILES.get("assignment")
            assdate= request.POST.get("adt")
            stdcourse = request.POST.get("stdcrs")
            stdname = request.POST.get("stdname")
            chobj=minorwork_tbl.objects.filter(an=assname)
            if chobj:
                user = request.session['mpusername']
                passw = request.session['mppassword']
                mobj=mp.objects.filter(email=user,passwd=passw)
                return render(request, 'minoruploadwork.html', {"success": False,"data":mobj})

            obj = minorwork_tbl.objects.create(an=assname, assignment=assign, adt=assdate, stdcrs=stdcourse, stdname=stdname)
            obj.save()
            if obj:
                t = "successfully registered"
                user = request.session['mpusername']
                passw = request.session['mppassword']
                mobj=mp.objects.filter(email=user,passwd=passw)

                return render(request, 'minoruploadwork.html', {"success": True,"data": mobj})
            else:
                t = " not successfully registered"
                user = request.session['mpusername']
                passw = request.session['mppassword']
                mobj=mp.objects.filter(email=user,passwd=passw)
                return render(request, 'minoruploadwork.html', {"success": False,"data":mobj})

        else:
            user = request.session['mpusername']
            passw = request.session['mppassword']
            if user == "" and passw == "":
                return redirect("/Minor_Programmer/")
            else:
                mobj=mp.objects.filter(email=user,passwd=passw)
                return render(request, 'minoruploadwork.html', {"data": mobj})







def viewminorwork(request):
    #tid=request.GET.get('tut_id')
    tidno=request.session['tutid']
    tu=tutorReg_tbl.objects.filter(id=tidno)
    if tu:
        for t in tu:
            crs=t.dpt
            print(crs)
        vmwobj=minorwork_tbl.objects.filter(stdcrs=crs)
    else:
        return redirect("/home")    



    return render(request, 'miass.html', {'data': vmwobj})
def deleteminwork(req):
    minwrk=req.GET.get('minwrkid')    
    if minwrk:
        obj=minorwork_tbl.objects.get(id=minwrk)
        obj.delete()
        return redirect("/Minor_Programmer/viewminorwork")

def download_file(request):
        # fill these variables with real values
        fl = request.GET.get('filename')
        file_path = os.path.join(settings.MEDIA_ROOT, fl)
        print(file_path)
        # pos=fl.index(".")
        # fnl=fl[0,pos+1]
        # filename =fnl+'.xls'

        # fl=open(fl_path,"r")
        # mime_type,_= mimetypes.guess_type(fl_path)
        # response = HttpResponse(fl, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/pdf')
                response['content-Disposition'] = 'inline;filname=' + os.path.basename(file_path)
                return response
        raise Http404
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("passw")
        obj=mp.objects.filter(email=username,passwd=password)
        if obj:
            #crs=course.objects.all()crs=course.objects.all()
            request.session['mpusername']=username
            request.session['mppassword']=password
            for ls in obj:
                stdid = ls.id
                request.session['mpid']=ls.id
            ap = appre_tbl.objects.filter(studentid=stdid)
            return redirect("/Minor_Programmer/home")
        else:
            request.session['mpusername']=""
            request.session['mppassword']=""
            msg="username or password incorrect"
            

            crs=course.objects.all()
            return render(request,'MinorLogin.html',{'lmsg':msg,'course':crs})
    else:
        msg=" "
        return render(request,'MinorLogin.html',{'lmsg':msg})
def shareprofile(request):
    obj = User_mp.objects.filter(username='appu123', passwd='1234adithya')
    msg = ""
    return render(request, 'shareprofile.html', {'data': obj, 'msg': msg})

def Course(request):
    course = Course.objects.filter(user=request.user)

    context = {'course':course}
def Live_Class(request):
    obj = Live_Class.objects.all()

def Worksmp(request):
    user=request.session['mpusername']
    passw=request.session['mppassword']
    obj=User_mp.objects.filter(email=user,passwd=passw)
    for t in obj:
        crs=t.mcs
        btc=t.batch
        nam=t.id
    
    wobj = Works_tbl.objects.filter(course=crs,std=nam)
    return render(request, 'works.html', {'data': wobj})   