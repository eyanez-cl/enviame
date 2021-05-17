import datetime
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


# Create your models here.
def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("1973-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo acepta fechas de ese rango")
    

   
    
class Envio(models.Model):
    fecha_de_nac = models.DateField()
    run = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, default="Chile")
    remitente = models.CharField(max_length=50)
    
    

    