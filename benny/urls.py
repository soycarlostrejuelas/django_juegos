"""
URL configuration for benny project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bennyapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("modificar_menu/",editar_menu),
    path("modificar_cli/<int:pk>/",editar_cliente, name="modificar_cliente"),
    path("modificar_jue/<int:pk>/",editar_juego, name="modificar_juego"),
    path("modificar_pla/<int:pk>/",editar_plataforma, name="modificar_plataforma"),
    path("editar_envio_cliente/",editar_envio_cliente),
    path("editar_envio_juego/",editar_envio_juego),
    path("editar_envio_plataforma/",editar_envio_plataforma),
    path("ingresar_menu/",ingresar_menu),
    path("ingresar_cliente_opc/",ingresar_cliente_opc),
    path("ingresar_cliente/",ingresar_cliente),
    path("ingresar_juego_opc/",ingresar_juego_opc),
    path("ingresar_juego/",ingresar_juego),
    path("ingresar_plataforma_opc/",ingresar_plataforma_opc),
    path("ingresar_plataforma/",ingresar_plataforma),
    path("ingresar_union_opc/",ingresar_union_opc),
    path("ingresar_union/",ingresar_union),
    path("buscar_menu/",buscar_menu),
    path("buscar_clientes/",buscar_cliente, name="buscar_cliente_form"),
    path("buscar_juegos/",buscar_juego, name="buscar_juego_form"),
    path("buscar_plataformas/",buscar_plataforma, name="buscar_plataforma_form"),
    path("eliminar_confirmar_cliente/<int:pk>/",confirmar_eliminacion_cliente),
    path("eliminar_cliente/<int:pk>/",eliminar_cliente),
    path("eliminar_confirmar_juego/<int:pk>/",confirmar_eliminacion_juego),
    path("eliminar_juego/<int:pk>/",eliminar_juego),
    path("eliminar_confirmar_plataforma/<int:pk>/",confirmar_eliminacion_plataforma),
    path("eliminar_plataforma/<int:pk>/",eliminar_plataforma),


]
