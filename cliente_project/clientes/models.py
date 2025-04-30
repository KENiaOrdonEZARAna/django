from django.db import models

# Create your models here.

# Definimos el modelo Cliente
class Cliente(models.Model):
    # Nombre del cliente
    nombre = models.CharField(max_length=100)
    # Email del cliente, debe ser único
    email = models.EmailField(unique=True)
    # Teléfono del cliente
    telefono = models.CharField(max_length=15)
    # Dirección del cliente
    direccion = models.CharField(max_length=255)

    # Representación del objeto como una cadena
    def __str__(self):
        return self.nombre
    

