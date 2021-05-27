from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'demo.html')
from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html')