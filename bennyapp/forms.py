from django import forms
from .models import *

class modificar_cliente(forms.ModelForm):
    class meta:
        model=cliente
        fields=("nombre","edad","direccion","telefono","f_n")
class modificar_juego(forms.ModelForm):
    class meta:
        model=juego
        fields=("nombre","plataforma")
class modificar_c_j(forms.ModelForm):
    class meta:
        model=c_j
        fields=("cliente","juego")
class c_j_f(forms.ModelForm):
    class Meta:
        model=c_j
        fields=("cliente","juego")
class modificar_juego(forms.ModelForm):
    class meta:
        model=juego
        fields=("nombre","plataforma")
class juego_f(forms.ModelForm):
    class Meta:
        model=juego
        fields=("nombre","plataforma")
class modificar_plataforma(forms.ModelForm):
    class meta:
        model=plataforma
        fields=("nombre",)
class cliente_f(forms.ModelForm):
    class Meta:
        model=cliente
        fields=("nombre","edad","direccion","telefono","f_n")
class plataforma_f(forms.ModelForm):
    class Meta:
        model=plataforma
        fields=("nombre",)
class buscar_cliente_form(forms.Form):
    nombre=forms.CharField(label='nombre del cliente',required=False)
class buscar_juego_form(forms.Form):
    nombre=forms.CharField(label="nombre del juego",required=False)
class buscar_plataforma_form(forms.Form):
    nombre=forms.CharField(label="nombre de la plataforma",required=False)
