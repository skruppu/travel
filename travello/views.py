from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination
# Create your views here.

def index(request):
    des=Destination.objects.all()
    return render (request,"index.html",{'des':des})
