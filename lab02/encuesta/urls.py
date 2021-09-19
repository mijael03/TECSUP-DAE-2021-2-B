from django.urls import path

from . import views

app_name='encuesta'

urlpatterns = [
    path('',views.index,name='index'),
    path('enviar',views.enviar,name='enviar'),
    path('numbers',views.numbers, name='numbers'),
    path('calc',views.calcular,name='calc'),
    path('cilindro',views.cilindro,name='cilindro'),
    path('result',views.result,name='result')
]