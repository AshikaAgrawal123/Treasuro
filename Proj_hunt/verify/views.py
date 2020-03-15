from django.shortcuts import render
from django.contrib.auth import get_user_model,authenticate,login

from .models import verification
User=get_user_model()

def gen(request):
	objs=verification.objects.all()
	li=[]
	for i in objs:
		li.append(i.signid)
	data={
		'reg':li,
		'range':range(4)
	}
	return render(request,"Backend/gen.html",data)



