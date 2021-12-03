from django.http.response import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.

def homefunction(request):
    return HttpResponse("hai")

def aboutfunction(request):
    return render(request,'one.html')