from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
User=get_user_model()
# Create your models here.
class Profile(models.Model):
    leader=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    admission=models.CharField(null=True,max_length=100)
    # participant3=models.CharField(null=True,max_length=100)
    email=models.EmailField()
    # email2=models.EmailField(null=True)
    # email3=models.EmailField(null=True)
    # branch1=models.CharField(max_length=100)
    # branch2=models.CharField(null=True,max_length=100)
    # branch3=models.CharField(null=True,max_length=100)
    number=models.IntegerField()
    level=models.IntegerField(default=4)
    signid=models.CharField(max_length=12,null=True)
    attempts=models.IntegerField(default=0)
    password=models.CharField(max_length=1000,null=True,blank=True)
    points=models.IntegerField(default=0)
    freeze=models.BooleanField(default=False)
    lastsub = models.DateTimeField(auto_now=False)
    rules=models.BooleanField(default=False)#Seen Rules or not 
    q1=models.BooleanField(default=False)
    q2=models.BooleanField(default=False)
    q3=models.BooleanField(default=False)
    q4=models.BooleanField(default=False)
    q5=models.BooleanField(default=False)
    q6=models.BooleanField(default=False)
    q7=models.BooleanField(default=False)
    q8=models.BooleanField(default=False)
    q9=models.BooleanField(default=False)
    q10=models.BooleanField(default=False)
    poi=models.CharField(max_length=1000,default='')
    tuh=models.CharField(max_length=10000,default='')


    class Meta:
        ordering=['-points','lastsub']
    def __str__(self):
        return self.name

