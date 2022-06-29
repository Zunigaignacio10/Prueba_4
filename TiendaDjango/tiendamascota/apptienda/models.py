from django.db import models


class Producto(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name='Codigo')
    nombre = models.CharField(max_length=20, verbose_name='Nombre', default="")
    valor= models.CharField(max_length=25, verbose_name='Valor', default="")
    descripcion = models.CharField(max_length=50, verbose_name='descripcion', default="")
    

    def __str__(self):
        return self.codigo

class Cliente(models.Model):
    rut=models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=10, verbose_name='Nombre')
    correo=models.CharField(max_length=40, verbose_name='Correo')
    telefono=models.CharField(max_length=9, verbose_name='telefono', default="")
    direccion=models.CharField(max_length=40, verbose_name='direccion', default="")    
    

    def __str__(self):
        return self.rut