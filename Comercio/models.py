from django.db import models
from django.urls import reverse

# Create your models here.


class Producto(models.Model):
    idd = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 20)
    precio = models.CharField(max_length = 20)
    categoria = models.ForeignKey("Categoria", related_name='+',  on_delete=models.CASCADE,null = False,)
    def __str__(self):
        return str(self.nombre)

class Categoria(models.Model):
    idd = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.nombre)


class Proveedore(models.Model):
    nombre = models.CharField(max_length = 20)
    web = models.CharField(max_length = 20)
    rut = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 20)
    direccion = models.ForeignKey("Direccion", related_name='+',  on_delete=models.CASCADE,null = False,)
    producto = models.ForeignKey("Producto", related_name='+', on_delete=models.CASCADE,null = False,)
    def __str__(self):
        return str(self.nombre)

class Venta(models.Model):
    idd = models.CharField(max_length = 20)
    fecha = models.CharField(max_length = 20)
    montofinal = models.CharField(max_length = 20)
    descuento = models.CharField(max_length = 20)
    cliente = models.ForeignKey("Cliente", related_name='+',  on_delete=models.CASCADE,null = False,)
    def __str__(self):
        return str(self.fecha)

class Cliente(models.Model):
    nombre = models.CharField(max_length = 20)
    rut = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 20)
    direccion = models.ForeignKey("Direccion", related_name='+',  on_delete=models.CASCADE,null = False,)
    def __str__(self):
        return str(self.nombre)

class Direccion(models.Model):
    calle = models.CharField(max_length = 20)
    numero = models.CharField(max_length = 20)
    comuna = models.CharField(max_length = 20)
    ciudad = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.calle)

