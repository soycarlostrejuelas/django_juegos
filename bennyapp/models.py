from django.db import models

class cliente(models.Model):
    nombre=models.CharField()
    edad=models.CharField()
    direccion=models.CharField()
    telefono=models.BigIntegerField()
    f_n=models.CharField()
    def __str__(self):
        texto='{0}'
        return texto.format(self.nombre)

class plataforma(models.Model):
    nombre=models.CharField()
    def __str__(self):
        texto='{0}'
        return texto.format(self.nombre)

class juego(models.Model):
    nombre=models.CharField()
    plataforma=models.ForeignKey(plataforma, on_delete=models.CASCADE)
    def __str__(self):
        texto='{0}'
        return texto.format(self.nombre)

class c_j(models.Model):
    cliente=models.ForeignKey(cliente, on_delete=models.CASCADE)
    juego=models.ForeignKey(juego, on_delete=models.CASCADE)
    def __str__(self):
        texto='{0}-{1}'
        return texto.format(self.cliente.nombre,self.juego.nombre)
# Create your models here.
