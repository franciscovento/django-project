from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
  return HttpResponse("Hello, Django!");  

def about(request):
  return HttpResponse("This is a Django website created by me.");