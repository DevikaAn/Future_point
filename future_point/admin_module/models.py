from django.db import models

# Create your models here.
class notification_tbl(models.Model):
    notititle=models.CharField(max_length=100)
    notidate=models.DateField()
    msg=models.CharField(max_length=100)
class admin_tbl(models.Model):
    username=models.CharField(max_length=50)
    passw=models.CharField(max_length=50)
class course(models.Model):
    cname=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    crs_img=models.FileField(upload_to="course")


