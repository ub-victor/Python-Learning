from  django.http import HttpResponse
from django.shortcuts import render
# django is the package / shortcuts the modules in modules shortcuts with call render
# Create your views here.


def  index(request, response):
    return HttpResponse("Hello World")