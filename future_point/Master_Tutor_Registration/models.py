from django.db import models

# Create your models here.
class User_mtr(models.Model):
    mtname=models.CharField(max_length=100)
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
    batch=models.CharField(max_length=100)
    up_date=models.DateField(auto_now=True)
class minorwork_tbl(models.Model):
    an=models.CharField(max_length=100)
    adt=models.DateTimeField(auto_now=True)
    assignment=models.FileField(upload_to="mwork")
    stdcrs=models.CharField(max_length=100)
    stdname=models.CharField(max_length=100)