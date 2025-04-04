from django.db import models
from django.contrib.auth.models import User

# aqui se define el modelo de la notificación



class Notification(models.Model):
    RECEPCIONISTAS = [
        ('amanda', 'Amanda González'),
        ('wanda', 'Wanda Pastor'),
    ]

    #agregar el campo de usuario que recibe la notificación

    fecha_recepcion = models.DateField()
    hora_recepcion = models.TimeField()
    entidad_emisora = models.CharField(max_length=255)
    numero_expediente = models.CharField(max_length=100)
    dirigido_a = models.CharField(max_length=255)
    recepcionista = models.CharField(max_length=10, choices=RECEPCIONISTAS)
    
    entregado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    hora_entrega = models.TimeField(null=True, blank=True)

    