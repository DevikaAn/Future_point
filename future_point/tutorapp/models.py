from django.db import models
from Minor_Programmer.models import User_mp

# Create your models here.
class tutorReg_tbl(models.Model):
    tname=models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)
    dpt=models.CharField(max_length=100)
    desi=models.CharField(max_length=100)
class Notes_tbl(models.Model):
    title=models.CharField(max_length=100)
    dt = models.CharField(max_length=100)
    url = models.FileField(upload_to="notes")
    crs = models.CharField(max_length=100)
    std = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    batch=models.CharField(max_length=100)
class Works_tbl(models.Model):
    notes=models.FileField(upload_to="works")
    wt=models.CharField(max_length=100)
    wdt=models.DateField()
    course=models.CharField(max_length=100)
    std=models.CharField(max_length=100)
    
class appre_tbl(models.Model):
    studentid=models.ForeignKey(User_mp, on_delete=models.CASCADE)
    studname=models.CharField(max_length=100)
    appreciation=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    colour=models.CharField(max_length=100)
# Live Classes
class Live_Class(models.Model):
     url = models.CharField(max_length=100)
     bthname = models.CharField(max_length=25)
     btime = models.CharField(max_length=25)
     title = models.CharField(max_length=100)
     def __str__(slef):
         return self.bthname

class MeetCab(models.Model):
    stdid=models.CharField(max_length=100)
    btch=models.CharField(max_length=100) 
    stdname=models.CharField(max_length=100)

    def __str__(self):
        return self.stdname
class Sendlink(models.Model):
    url=models.CharField(max_length=100) 
    batch=models.CharField(max_length=100)
    btime = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    def __str__(request):
        return self.batch
class videoClass(models.Model):
    title = models.CharField(max_length=100)  
    video_file=models.FileField(upload_to="class_video")
    course=models.CharField(max_length=100)
    batch=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

