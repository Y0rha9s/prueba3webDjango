from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'region'

class Contact(models.Model):
    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    correo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    sugerencia = models.CharField(max_length=100)
    
    class Meta:
        managed = True
        db_table = 'Contact'
        
class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    
    class Meta:
        managed = True
        db_table = 'Usuario'