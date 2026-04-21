from  django.http import HttpResponse
from django.shortcuts import render
# django is the package / shortcuts the modules in modules shortcuts with call render
# Create your views here.

# /products -> index
#  URL = Unoform Resource Locator (Address)
def  index(request):
    return HttpResponse("Hello World")


def  new(request):
    return HttpResponse("New products")