from django.shortcuts import render,redirect
from  django.http import HttpResponse
from . models import tutorReg_tbl as  tut
from  Minor_Programmer.models import User_mp as mp
from Master_Tutor_Registration.models import Notes_tbl,Works_tbl
from tutorapp.models import appre_tbl,Sendlink,videoClass
from admin_module.models import course as co
from django.db.models import Q

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import os
from django.http.response import Http404
import random
from django.conf import settings
from django.core.mail import send_mail
from admin_module.models import course as co
from Minor_Programmer.models import User_mp


def password_gen():
    sp=['@','#','$','%','&','*',')']
    
    print(ord('A'),ord('Z'),ord('a'),ord('z'))
    
    codeno=""

    for i in range(0,2):
        j=random.randint(0,6)
        
        codeno=codeno+chr(random.randrange(65,90))+sp[j]+str(random.randint(0,9))
    return codeno       

def tutemail(request):
    if request.method=="POST":

        subject=request.POST.get("subjecttut")
        msg=request.POST.get("messagetut")
        to=request.POST.get("totut")
        res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
        if(res==1):
            msg="mail send successfully"
            return render(request, 'temail.html', {'msg': msg})
        else:
            msg="mail could not send"
            return render(request, 'temail.html', {'msg': msg})
    else:
        msg=" "
        return render(request,'temail.html',{'msg':msg})
# Create your views here.
#def home(request):
    #return HttpResponse("hello")
def home(request):
    return render(request,'tutor_homepage.html')
def tureg(request):
    if request.method == "POST":
        a = request.POST.get("tname")
        b = request.POST.get("address")
        c = request.POST.get("phoneno")
        e = request.POST.get("dpt")
        # f = request.POST.get("username")
        # g = request.POST.get("passwd")
        h = request.POST.get("email")
        i = request.POST.get("gender")
       # j = request.POST.get("desi")
        print(a,b)
        # rno = random.randrange(499, 699)
        # rno = str(rno)
        # passw =chr(random.randrange(0,128))+ra[0:3] + rno
        # print(passw)
        passwd = password_gen()

        obj = tut.objects.create(tname=a, address=b, phoneno=c, dpt=e, username=h, passwd=passwd,
                                     email=h, gender=i, desi="des")
        obj.save()
        if obj:
            subject = "Username and Password"
            msg = "Your Username:" + h + "\n Password:" + passwd + "\n Login using this link http://127.0.0.1:8000/tutorapp/"
            to = h
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
            if res:
                l = "successfully registered mail send"
            else:
                l="registered  successfully mail not send"

            return render(request, 'Tutor_Registration.html', {"success": l})
        else:
            # l = " not successfully registered"
            return render(request, 'Tutor_Registration.html', {"success":" Not successfully registered mail send"})

    else:
        crs=co.objects.all()
        return render(request, 'Tutor_Registration.html',{'course':crs})
def notes(request):
    return render(request,'notes.html')
def loginpage(request):
    return render(request,'TutorLogin.html')

# Create your views
def home(request):
    user=request.session['username']
    passw=request.session['password']
    if user==""and passw=="":
        return redirect("/tutorapp/")
    else:

        return render(request,'tutor_homepage.html')
def logout(request):
    request.session['username']=""
    request.session['password']=""
    return redirect("/Minor_Programmer/")



def index(request):
    return render(request, 'index.html')


def tregis(request):
    trobj = tut.objects.all()
    frm=request.GET.get('frm')
    print(frm)
    if frm=='ADM':
        return render(request, 'admintutor.html', {'data': trobj})
    else:
        return render(request, 'tutordetails.html', {'data': trobj})

    # return render(request, 'tutordetails.html', {'data': trobj})
    #


def edt(request):
    idno = request.GET.get("tutid")
    obj = tut.objects.filter(id=idno)
    return render(request, 'edit.html', {'data': obj})


def update(request):
    if request.method == "POST":
        a = request.POST.get("tname")
        b = request.POST.get("address")
        c = request.POST.get("phoneno")
        e = request.POST.get("dpt")
        f = request.POST.get("username")
        g = request.POST.get("passwd")
        h = request.POST.get("email")
        i = request.POST.get("gender")
        j = request.POST.get("desi")
        idno = request.POST.get("idno")
        upobj = tut.objects.get(id=idno)
        upobj.tname = a
        upobj.address = b
        upobj.phoneno = c
        upobj.dpt = e
        upobj.username = f
        upobj.passwd = g
        upobj.email = h
        if i!="":
            upobj.gender = i
        upobj.desi = j
        upobj.save()
        return redirect("/tutorapp/tutdetails")


def uploadnotes(request):
    if request.method=="POST":
        title=request.POST.get("tt")
        note=request.FILES.get("notes")
        date=request.POST.get("dt")
        course=request.POST.get("course")
        standard=request.POST.get("std")
        obj = Notes_tbl.objects.create(title=title, url=note, dt=date, crs=course, status=standard)
        obj.save()
        if obj:
            s = "successfully registered"
            obj= mp.objects.all()
            crs=co.objects.all()

            return render(request, 'uploadworkT.html', {"success": t,"course":crs,'std':ob})

           
        else:
            s = " not successfully registered"
            obj= mp.objects.all()
            crs=co.objects.all()

            return render(request, 'uploadworkT.html', {"success": t,"course":crs,'std':ob})

    else:
        crs = co.objects.all()
        stud=mp.objects.all()

        return  render(request,'uploadnotesT.html',{'data':crs,'stud':stud})

def uploadworks(request):
        if request.method == "POST":
            wtitle = request.POST.get("wt")
            work = request.FILES.get("works")
            wdate = request.POST.get("wdt")
            course = request.POST.get("course")
            stand = request.POST.get("std")
            obj = Works_tbl.objects.create(wt=wtitle, notes=work, wdt=wdate, course=course, std=stand)
            obj.save()
            if obj:
                t = "successfully registered"
                obj= mp.objects.all()
                crs=co.objects.all()

                return render(request, 'uploadworkT.html', {"success": t,"course":crs,'std':ob})
            else:
                t = " not successfully registered"
                
                obj= mp.objects.all()
                crs=co.objects.all()

                return render(request, 'uploadworkT.html', {"success": t,"course":crs,'std':ob})
                

        else:
            obj= mp.objects.all()
            crs=co.objects.all()
            return render(request, 'uploadworkT.html',{"course":crs,'std':obj})

def Notes(request):
            idn=request.GET.get("mpid")
            
            noobj = Notes_tbl.objects.all()
            return render(request, 'notes.html', {'data': noobj})


def Works(request):
    wobj = Works_tbl.objects.all()
    return render(request, 'works.html', {'data': wobj})

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
        obj=tut.objects.filter(username=username,passwd=password)
        if obj:
            request.session['username']=username
            request.session['password']=password
            return redirect("/tutorapp/home")
        else:
            request.session['username']=""
            request.session['password']=""
            msg="check your  username and password"

            return render(request,'TutorLogin.html',{'lmsg':msg})
    else:
        msg=" "
        return render(request,'TutorLogin.html',{'lmsg':msg})
def appre(request):
    stid=request.GET.get("sdtid")
    colr=request.GET.get("colr")
    mp1=mp.objects.filter(id=stid)
    for ls  in mp1:
        stdname=ls.mpname
    chck = appre_tbl.objects.filter(studname=stdname, colour=colr)
    if chck:
        msg = "Already send"
        return redirect("/Minor_Programmer/mpdetailsT?msg=Already send")


    if colr=="red":
        url="images/badge.png"
    if colr=="green":
        url="images/ribbon.png"
    if colr=="blue":
        url="images/best-seller.png"

    frkid=mp.objects.get(id=stid)
    print(frkid)
    obj=appre_tbl.objects.create(studentid=frkid,studname=stdname,appreciation=url,colour=colr)
    if obj:
        obj.save()
        msg="Appreciation send"
        return redirect("/Minor_Programmer/mpdetailsT?msg=Appreciation send")
    else:
        msg = "Error in Sending Appreciation "
        return redirect("/Minor_Programmer/mpdetailsT?msg=Error in Sending Appreciation")
def delt(request):
    idno=request.GET.get("idn")
    mast=tut.objects.get(id=idno)
    mast.delete()
    return redirect("/tutorapp/tutdetails")

def gmeet(request):
    if request.method == "POST":
        # a = request.POST.get("bthname")
        # b = request.POST.get("stdname")
        # c = request.POST.get("btime")
        # d = request.POST.get("url")
        # obj = Live_Class.objects.create(bthname=a,stdname=b,btime=c,url=d)
        # obj.save()
        # if obj:
        #     l = "Successfully Registered"
        #     return render(request,'gmeet.html',{"success":l})
        # else:
        #     l = "Not Registered Successfully"
        #     return render(request,'gmeet.html',{"success":l})
        bt=request.POST.get('batch')
        x=request.POST.getlist('std')
        l=len(x)
        for i in range(0,l):
            print(x[i])
            std=mp.objects.get(id=int(x[i]))
            if std:
                std.batch=bt
                std.save()
                print("save")

        print(x)
        std=mp.objects.filter(~Q(batch=1))
        obj2 = Sendlink.objects.all()
        std=mp.objects.all()
        return render(request,'gmeet.html',{'data':std,'live':obj2})


    else:
        obj2 =Sendlink.objects.all()
        std=mp.objects.all()
        return render(request,'gmeet.html',{'data':std,'live':obj2})
def urlsve(request):
    if request.method=="POST":
        title=request.POST.get('tit')
        url=request.POST.get('url')
        batch=request.POST.get('batch')
        student=request.POST.get('student')
        bttime=request.POST.get('time')
        
        lv=Sendlink.objects.create(url=url,batch=batch,btime=bttime,title=title)
        if lv:
            lv.save()
            obj2 =Sendlink.objects.all()
            std=mp.objects.all()

            return render(request,'gmeet.html',{'msg':"Successfully Registered",'data':std,'live':obj2})

def video_upload(req):
    if  req.method=="POST":
        title=req.POST.get("title")
        vfile=req.FILES.get("vid")
        course=req.POST.get("course")
        batch=req.POST.get("batch")
        obj=videoClass.objects.create(title=title,video_file=vfile,course=course,batch=batch)
        if obj:
            obj.save()
            return render(req,'video_upload.html',{'msg':"uploaded Successfully"})
    else:        

        crs=co.objects.all() 
        btc=User_mp.objects.all()
        return render(req,'video_upload.html',{'msg':"", 'course':crs,'batch':btc})            

def video(req):
    try:
        if req.GET.get('batch'):
            b=req.GET.get('batch')
            
            vid=videoClass.objects.filter(batch=b)
            return render(req,'video.html',{'video':vid})
        else:
            return HttpResponse("No Video Upload")    
    except Exception as e:
         return HttpResponse("No Batch created No Video Upload")        
    return HttpResponse(" No Batch created No Video Upload")     
