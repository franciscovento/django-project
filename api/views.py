from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ping(request): 
  if(request.method == "POST"):
    return HttpResponse("pong")