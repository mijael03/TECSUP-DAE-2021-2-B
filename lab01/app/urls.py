from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suma/<int:a>/<int:b>',views.suma,name='suma'),
    path('resta/<int:a>/<int:b>',views.resta,name='resta'),
    path('multiply/<int:a>/<int:b>',views.multiply,name='multiplicación'),
]
