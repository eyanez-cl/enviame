import datetime

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import  Envio


def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("1973-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo acepta fechas de ese rango")

class FormularioEnvio(forms.Form):
    remitente = forms.CharField(
        validators= [
            validators.MinLengthValidator( 3, 'Su nombre debe tener al menos 3 caracteres')
        ]
    )
    direccion = forms.CharField(
        validators = [ 
                        validators.MinLengthValidator( 3, 
						    "La Direccion no puede ser de menos de 3 letras"),
                        validators.MaxLengthValidator( 30, 
						    "El modelo no puede ser de más de 30 letras") ])
    
    run = forms.CharField()
    fecha_nacimiento = forms.DateField( validators = [validar_fecha])