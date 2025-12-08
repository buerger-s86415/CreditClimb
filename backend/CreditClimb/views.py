from django.shortcuts import render, HttpResponse
from templates import *

def home(request):
    return render(request,'home.html')