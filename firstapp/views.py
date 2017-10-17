from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import UserDetails,userHome
# Create your views here.

def index(request):
    my_dict = {'insert_me' : "hello i am from views.py"}
    return render(request,'firstapp/index.html',context=my_dict)

def login(request):
    # my_dict = {'insert_me' : "hello"}
    return render(request,'firstapp/login.html')
