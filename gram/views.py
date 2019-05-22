from django.shortcuts import render,redirect
from .models import user
from .forms import *


# Create your views here.
def login(request):
    context = {}
    return render(request, "login.html" , context)

def index(request):
    context={}   
    return render(request, "index.html" , context)

