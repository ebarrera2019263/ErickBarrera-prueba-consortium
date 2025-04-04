from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-fecha_recepcion', '-hora_recepcion')
    serializer_class = NotificationSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        
        # Solo enviar correo si se ha completado la entrega
        if instance.entregado_a and instance.fecha_entrega and instance.hora_entrega:
            self.send_notification_email(instance)

    def send_notification_email(self, instance):
        subject = "Notificación recibida: {}".format(instance.numero_expediente)
        message = (
            f"Entidad emisora: {instance.entidad_emisora}\n"
            f"Fecha de recepción: {instance.fecha_recepcion} {instance.hora_recepcion}\n"
            f"Dirigido a: {instance.dirigido_a}\n"
            f"Recepcionista: {dict(Notification.RECEPCIONISTAS).get(instance.recepcionista)}\n"
            f"Entregado a: {instance.entregado_a.get_full_name()}\n"
            f"Fecha de entrega: {instance.fecha_entrega} {instance.hora_entrega}\n"
        )
        send_mail(
            subject,
            message,
            'no-reply@tuapp.com',  # Cambia esto por el email del remitente
            ['ptoribio@consortiumlegal.com'],
            fail_silently=False,
        )

