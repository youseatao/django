from django.http import HttpResponse
from django.shortcuts import render
import time

def first_page(request):
	return HttpResponse("<p>hello world %s</p>"%time.asctime())
	
def timeoffset(request, offset):
	sTime = "the offset is %s"%offset	
	return render(request, "test.html", {"person_name":sTime})

