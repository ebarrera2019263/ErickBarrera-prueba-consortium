from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'entidad_emisora', 'dirigido_a', 'fecha_recepcion', 'recepcionista', 'entregado_a')
    list_filter = ('recepcionista', 'fecha_recepcion')
    search_fields = ('numero_expediente', 'dirigido_a', 'entidad_emisora')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.entregado_a and obj.fecha_entrega and obj.hora_entrega:
            subject = f"Notificación recibida: {obj.numero_expediente}"
            message = (
                f"Entidad emisora: {obj.entidad_emisora}\n"
                f"Fecha de recepción: {obj.fecha_recepcion} {obj.hora_recepcion}\n"
                f"Dirigido a: {obj.dirigido_a}\n"
                f"Recepcionista: {dict(obj.RECEPCIONISTAS).get(obj.recepcionista)}\n"
                f"Entregado a: {obj.entregado_a.get_full_name() or obj.entregado_a.username}\n"
                f"Fecha de entrega: {obj.fecha_entrega} {obj.hora_entrega}\n"
            )
            print(" Correo desde admin:\n", message)

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,                    # Remitente
                [settings.NOTIFICATION_RECIPIENT],           # Destinatario oficial
                fail_silently=False,
            )
        else:
            print(" Admin: Correo no enviado - Faltan datos")
