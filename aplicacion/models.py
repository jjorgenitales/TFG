from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    clave = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    cp = models.CharField(max_length=10)
    tipo = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.nombre