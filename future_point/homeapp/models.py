from django.db import models

# Create your models here.
class User_tb3_nw(models.Model):
    studentname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    gname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=100)
    gphno=models.CharField(max_length=100)