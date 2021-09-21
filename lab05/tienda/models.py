from django.db import models
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6,decimal_places=2)
    stock=models.IntegerField(default=0)
    pub_date= models.DateTimeField('date published')
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=9)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    birth_date=models.DateTimeField('date of birth')
    pub_date=models.DateTimeField('date published')