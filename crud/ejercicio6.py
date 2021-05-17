import random
from datetime import datetime

def calculo_tiempo_espera(km):
    fecha_de_envio = datetime.now()
    
    datetime.timedelta(days=1)
    
    
    if km <= 100:
       fec_recivo = fecha_de_envio 
    elif km >= 200:
       fec_recivo = fecha_de_envio + datetime.timedelta(days=1)
    elif km >= 300:
        fec_recivo = fecha_de_envio + datetime.timedelta(days=1)
    elif km >= 400:
        fec_recivo= fecha_de_envio + datetime.timedelta(days=2)
    elif km >=500:
        fec_recivo=  fecha_de_envio + datetime.timedelta(days=3)
        
        return fec_recivo
        
             
        
'''
respecto al ejercicio 7 donde se solicita actualizar los sueldos de empleados que ganen
5000 o menos, de acuerdo al reajuste anual del continente
no tengo sql en mi computador y me tome la libertad de crear las ablas en postgres.


'''