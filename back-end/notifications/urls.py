from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NotificationViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'notificaciones', NotificationViewSet, basename='notificacion')
router.register(r'usuarios', UsuarioViewSet, basename='usuario') 

urlpatterns = [
    path('', include(router.urls)),
]
