from rest_framework import serializers
from .models import Notification
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name'] 



class NotificationSerializer(serializers.ModelSerializer):
    entregado_a = UserSerializer(read_only=True)
    entregado_a_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='entregado_a', write_only=True, required=False
    )



    class Meta:
        model = Notification
        fields = [
            'id',
            'fecha_recepcion',
            'hora_recepcion',
            'entidad_emisora',
            'numero_expediente',
            'dirigido_a',
            'recepcionista',
            'entregado_a',
            'entregado_a_id',
            'fecha_entrega',
            'hora_entrega'
        ]