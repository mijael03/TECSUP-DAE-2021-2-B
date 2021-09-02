from django.shortcuts import render
from django.shortcuts import get_object_or_404,render 
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Opcion,Pregunta
# Create your views here.
def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'encuesta/index.html',context)

def detalle(request,pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request,'encuesta/detalle.html', {'pregunta':pregunta})

def votar(request,pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        selected_option = pregunta.opcion_set.get(pk=request.POST['opcion'])
    except(KeyError,Opcion.DoesNotExist):
        return render(request, 'encuesta/detalle.html', {
            'pregunta' : pregunta,
            'error_message' : "No has seleccionado una opcion",
        })
    else:
        selected_option.votos+=1
        selected_option.save()
        return HttpResponseRedirect(reverse('encuesta:results', args=(pregunta.id,)))

def results(request,pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request,'encuesta/results.html', {'pregunta':pregunta})

