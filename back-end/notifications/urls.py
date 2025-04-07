from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.models import User

from .views import NotificationViewSet, UsuarioViewSet

# 
def create_admin():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )

create_admin()

# 📦 Rutas
router = DefaultRouter()
router.register(r'notificaciones', NotificationViewSet, basename='notificacion')
router.register(r'usuarios', UsuarioViewSet, basename='usuario') 

urlpatterns = [
    path('', include(router.urls)),
]
