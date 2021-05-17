import json
import datetime
from django.shortcuts import render, redirect
from .forms import FormularioEnvio
from django.conf import settings
from .models import Envio

# Create your views here.


def context_lista_envios():
    filename = '/crud/data/envios.json'
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        envios = json.load(file)
        #ordenamiento de envios en el html
        envios['envios']= sorted(envios['envios'], key=lambda k: k['identificador'])
        print(envios['envios'])
        context = {'lista_envios': envios['envios']}
        return context 
    
# C de crud con JSON
def crear_envio(request):
    
    if request.method == "GET":
        formulario = FormularioEnvio()
        context = {'formulario': formulario}
        context.update(context_lista_envios())
        print(context)
        return render(request, 'crud/crear_envio.html', context)

    elif request.method == "POST":
        print("El POST contiene:", request.POST)

        formulario_devuelto = FormularioEnvio(request.POST)

        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha_compra']=datos_formulario['fecha_compra'].strftime("%Y-%m-%d")
            print("Los datos limpios del formulario son:", datos_formulario)
            filename= "/crud/data/envios.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data=json.load(file)
                nuevo_ultimo_identificador = int(data['ultimo_identificador']) + 1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['envios'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            
            return redirect('crud:crear_envio')
        else:
            context = {'formulario': formulario_devuelto}
            context.update(context_lista_envios())
            return render(request, 'crud/crear_envio.html', context)
        

#R de crud (leer)
def lista_envios(request):
    context = context_lista_envios()
    return render(request, 'crud/crear_envio.html', context)


# U de CRUD con archivo JSON
def editar_envio(request, identificador):

    if request.method == "GET":
        filename= "/crud/data/envios.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
        for envio in data['envio']:
            if int(envio['identificador'])==int(identificador):
                break
        formulario = FormularioEnvio(initial=envio)
        context = {'formulario': formulario, 'identificador': identificador}
        return render(request, 'crud/editar_enviohtml', context)

    elif request.method == "POST":
        print("El POST contiene:", request.POST)
        formulario_devuelto = FormularioEnvio(request.POST)
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha_compra']=datos_formulario['fecha_compra'].strftime("%Y-%m-%d")
            filename= "/crud/data/envios.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data=json.load(file)
            for envio in data['envios']:
                if int(envio['identificador'])==int(identificador):
                    data['envios'].remove(envio)
                    datos_formulario['identificador'] = envio['identificador']
                    data['envios'].append(datos_formulario)
                    break
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            return redirect('crud:lista_envios')
        else:
            context = {'formulario': formulario_devuelto}
            return render(request, 'crud/editar_envio.html', context)


# D de CRUD con archivo JSON
def eliminar_envio(request, identificador):

    if request.method == "GET":
        context = {'identificador': identificador}
        return render(request, "crud/eliminar_envio.html", context)

    if request.method == "POST":
        filename= "/curd/data/envios.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
        for envio in data['envios']:
            if int(envio['identificador'])==int(identificador):
                data['envios'].remove(envio)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(data, file)
        
        return redirect('crud:lista_envios')