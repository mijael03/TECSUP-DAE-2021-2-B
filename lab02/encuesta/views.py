from django.shortcuts import render
import math

# Create your views here.
def index(request):
    context = {
        'titulo': 'Formulario',
    }
    return render(request,'encuesta/formulario.html',context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html',context)

def numbers(request):
    return render(request,'encuesta/numbers.html')

def calcular(request):
    n1=request.POST['number1']
    n2=request.POST['number2']
    operation=request.POST['operation']
    if(operation=="resta"):
        result=int(n1)-int(n2)
    elif(operation=="suma"):
        result=int(n1)+int(n2)
    elif(operation=="multiplicacion"):
        result=int(n1)*int(n2)
    context = {
        'number1': n1,
        'number2': n2,
        'operation': operation,
        'result': result,
    }
    return render(request, 'encuesta/result.html',context)

def cilindro(request):
    return render(request,'encuesta/cilindro.html')

def result(request):
    pi=math.pi
    h=request.POST['altura']
    r=float(request.POST['diametro'])/2
    result=pi*float(h)*(r**2)
    context = {
        'result': result,
    }
    return render(request,'encuesta/volumen.html',context)