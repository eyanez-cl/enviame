from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('crear_envio', views.crear_envio, name='crear_envio'),
    path('lista_envios', views.lista_envios, name='lista_envios'),
    path('<identificador>/editar_envio', views.editar_envio, name='editar_envio'),
    path('<identificador>/borrar_envio', views.eliminar_envio, name='eliminar_envio'),
    ]
