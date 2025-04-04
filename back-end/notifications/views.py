from rest_framework import viewsets
from django.core.mail import send_mail
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-fecha_recepcion', '-hora_recepcion')
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        print(" Creando notificación...")

        if instance.entregado_a and instance.fecha_entrega and instance.hora_entrega:
            print(" Enviando correo desde perform_create...")
            self.send_notification_email(instance)
        else:
            print(" Correo NO enviado - Faltan datos de entrega (entregado_a, fecha_entrega, hora_entrega)")

    def perform_update(self, serializer):
        instance = serializer.save()
        print(" Editando notificación...")

        if instance.entregado_a and instance.fecha_entrega and instance.hora_entrega:
            print(" Enviando correo desde perform_update...")
            self.send_notification_email(instance)
        else:
            print(" Correo NO enviado - Faltan datos de entrega (entregado_a, fecha_entrega, hora_entrega)")

    def send_notification_email(self, instance):
        subject = f"Notificación recibida: {instance.numero_expediente}"
        message = (
            f"Entidad emisora: {instance.entidad_emisora}\n"
            f"Fecha de recepción: {instance.fecha_recepcion} {instance.hora_recepcion}\n"
            f"Dirigido a: {instance.dirigido_a}\n"
            f"Recepcionista: {dict(Notification.RECEPCIONISTAS).get(instance.recepcionista)}\n"
            f"Entregado a: {instance.entregado_a.get_full_name()}\n"
            f"Fecha de entrega: {instance.fecha_entrega} {instance.hora_entrega}\n"
        )
        print(" Contenido del correo:\n", message)

        send_mail(
            subject,
            message,
            'alamedagta21@gmail.com',  # o 'no-reply@tuapp.com'
            ['ptoribio@consortiumlegal.com'],  # Cambiar a correo oficial al final
            fail_silently=False,
        )
