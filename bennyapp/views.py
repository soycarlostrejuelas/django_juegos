from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *

def home(request):
    todo=c_j.objects.select_related("cliente","juego__plataforma").all()
    return render(request, 'index.html', {"data":todo})

def editar_cliente(request,pk):
    cli=get_object_or_404(cliente,pk=pk)
    if request.method == 'POST':
        form = cliente_f(request.POST, instance=cli)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= cliente_f(instance=cli)
        return render(request, 'modificar/modificar_cli.html', {'form': form})

def editar_juego(request,pk):
    jue=get_object_or_404(juego,pk=pk)
    if request.method == 'POST':
        form = juego_f(request.POST, instance=jue)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= juego_f(instance=jue)
        return render(request, 'modificar/modificar_jue.html', {'form': form})


def editar_plataforma(request,pk):
    pla=get_object_or_404(plataforma,pk=pk)
    if request.method == 'POST':
        form = plataforma_f(request.POST, instance=pla)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= plataforma_f(instance=pla)
        return render(request, 'modificar/modificar_pla.html', {'form': form})

def editar_menu(request):
    cli=cliente.objects.all()
    jue=juego.objects.all()
    pla=plataforma.objects.all()
    return render(request, "modificar/modificar_menu.html", {"clientes":cli,"juegos":jue,"plataforma":pla})

def editar_envio_cliente(request):
    cli_id=request.POST["cliente"]
    direccion="/modificar_cli/{}/".format(cli_id)
    return redirect(direccion)

def editar_envio_juego(request):
    cli_id=request.POST["juego"]
    direccion="/modificar_jue/{}/".format(cli_id)
    return redirect(direccion)

def editar_envio_plataforma(request):
    cli_id=request.POST["plataforma"]
    direccion="/modificar_pla/{}/".format(cli_id)
    return redirect(direccion)

def ingresar_menu(request):
    return render(request, "ingresar/ingresar_menu.html",{})

def ingresar_cliente_opc(request):
    return render(request, "ingresar/ingresar_cliente_opc.html",{})

def ingresar_cliente(request):
    nom=request.POST['nombre']
    tele=request.POST["telefono"]
    edad=request.POST["edad"]
    dire=request.POST["direccion"]
    fn=request.POST["F_N"]
    ingresar=cliente.objects.create(nombre=nom,telefono=tele,edad=edad,direccion=dire,f_n=fn)
    return redirect('/ingresar_cliente_opc/')

def ingresar_juego_opc(request):
    plata=plataforma.objects.all()
    return render(request, "ingresar/ingresar_juego_opc.html",{"plataforma":plata})

def ingresar_juego(request):
    nom=request.POST['nombre']
    plata=request.POST["plataforma"]
    ingresar=juego.objects.create(nombre=nom,plataforma_id=plata)
    return redirect('/ingresar_juego_opc/')

def ingresar_plataforma_opc(request):
    return render(request, "ingresar/ingresar_plataforma_opc.html",{})

def ingresar_plataforma(request):
    nom=request.POST['nombre']
    ingresar=plataforma.objects.create(nombre=nom,)
    return redirect('/ingresar_plataforma_opc/')

def ingresar_union_opc(request):
    cli=cliente.objects.all()
    jue=juego.objects.all()
    return render(request, "ingresar/ingresar_union_opc.html", {"clientes":cli,"juegos":jue})

def ingresar_union(request):
    clie=request.POST['cliente']
    jue=request.POST["juego"]
    ingresar=c_j.objects.create(cliente_id=clie, juego_id=jue)
    return redirect('/ingresar_plataforma_opc/')

def buscar_menu(request):
    return render(request,"buscar/buscar_menu.html",{})

def buscar_cliente(request):
    form=buscar_cliente_form(request.GET)
    if form.is_valid():
        nombre=form.cleaned_data.get('nombre')
        cli=cliente.objects.filter(nombre__icontains=nombre) if nombre else cliente.objects.all()
    return render(request, 'buscar/buscar_clientes.html',{"form":form,"clientes":cli})

def buscar_juego(request):
    form=buscar_juego_form(request.GET)
    if form.is_valid():
        nombre=form.cleaned_data.get('nombre')
        jue=juego.objects.filter(nombre__icontains=nombre) if nombre else juego.objects.all()
    return render(request, 'buscar/buscar_juegos.html',{"form":form,"juegos":jue})

def buscar_plataforma(request):
    form=buscar_plataforma_form(request.GET)
    if form.is_valid():
        nombre=form.cleaned_data.get('nombre')
        pla=plataforma.objects.filter(nombre__icontains=nombre) if nombre else plataforma.objects.all()
    return render(request, 'buscar/buscar_plataforma.html',{"form":form,"plataforma":pla})

def confirmar_eliminacion_cliente(request,pk):
    cli=get_object_or_404(cliente,pk=pk)
    return render(request,"eliminar/eliminar_confirmacion_cliente.html",{"aaa":cli})

def eliminar_cliente(request,pk):
    if request.method=='POST':
        cli=get_object_or_404(cliente,pk=pk)
        cli.delete()
        return redirect("/buscar_clientes/")
    else:
        return redirect("/buscar_clientes/")
#    
def confirmar_eliminacion_juego(request,pk):
    cli=get_object_or_404(juego,pk=pk)
    return render(request,"eliminar/eliminar_confirmacion_juego.html",{"aaa":cli})

def eliminar_juego(request,pk):
    if request.method=='POST':
        cli=get_object_or_404(juego,pk=pk)
        cli.delete()
        return redirect("/buscar_juegos/")
    else:
        return redirect("/buscar_juegos/")

def confirmar_eliminacion_plataforma(request,pk):
    cli=get_object_or_404(plataforma,pk=pk)
    return render(request,"eliminar/eliminar_confirmacion_plataforma.html",{"aaa":cli})

def eliminar_plataforma(request,pk):
    if request.method=='POST':
        cli=get_object_or_404(plataforma,pk=pk)
        cli.delete()
        return redirect("/buscar_plataformas/")
    else:
        return redirect("/buscar_plataformas/")
