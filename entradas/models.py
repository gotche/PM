from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.ForeignKey(User, unique=True)
    permisos = models.CharField(max_length=50,default="a")
    nombre = models.CharField(max_length=200)
    
    #Permisos
    # a = activo
    # b = pueden escribir entradas
    # c = subir nominas
    # d = administracion de material 
    # e = pedir material

    def __unicode__(self):
        return self.user.username
