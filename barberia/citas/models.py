from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
import string
import random

def id():
    var = string.ascii_uppercase
    varint = string.digits
    chars = var + varint
    return ''.join(random.choice(chars) for _ in range(8))

def validar_fecha_futura(value):
    """Valida que la fecha sea posterior a la fecha y hora actual"""
    if value <= timezone.now():
        raise ValidationError('La fecha debe ser posterior a la fecha y hora actual.')

class Barbero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(default='barbero@barberia.com')

    def __str__(self):
        return self.nombre
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
class Cita(models.Model):
    fecha = models.DateTimeField(validators=[validar_fecha_futura])
    identificador = models.CharField(max_length=8, unique=True, default=id)
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cliente_nombre = models.CharField(max_length=100, blank=False, null=False)
    cliente_telefono = models.CharField(max_length=15, blank=False, null=False)
    notas = models.TextField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], default='pendiente')
    
    def __str__(self):
        return f"{self.identificador} - {self.cliente_nombre}"
    
    def clean(self):
        """Validación adicional a nivel de modelo"""
        super().clean()