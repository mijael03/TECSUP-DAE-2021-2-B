from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse("Calculator App")
def suma(request,a,b):
    c=a+b
    return HttpResponse("El resultado de la suma es %s." % c)
def resta(request,a,b):
    c=a-b
    return HttpResponse("El resultado de la resta es %s." % c)
def multiply(request,a,b):
    c=a*b
    return HttpResponse("El resultado de la multiplicación es %s." % c) 
