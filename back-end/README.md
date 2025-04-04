# 📬 Sistema de Notificaciones Internas - Django

Este proyecto es una aplicación desarrollada en **Django + Django REST Framework** que permite registrar y controlar notificaciones físicas recibidas por una firma legal, incluyendo la entrega interna y notificación automática por correo electrónico.

---

## ⚙️ Tecnologías utilizadas

- Python 3.10
- Django 3.2.18
- Django REST Framework
- SQLite (base de datos por defecto)
- Gmail SMTP (para envío de correos)
- Django Admin

---

## 📦 Instalación y configuración

### 1. Clonar el proyecto

```bash
git clone https://github.com/tu-usuario/notificaciones-project.git
cd notificaciones-project


 1.Crear y activar un entorno virtual

 python -m venv env
env\Scripts\activate

2.Instalar dependencias

pip install -r requirements.txt


3. Migraciones

python manage.py makemigrations
python manage.py migrate

4. Crear superusuario
python manage.py createsuperuser


5. Configuración del correo (Gmail)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_correo@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña_de_aplicación'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Destinatario oficial
NOTIFICATION_RECIPIENT = 'ptoribio@consortiumlegal.com'


Acceso al panel de administración

http://127.0.0.1:8000/admin/

Desarrollado por: Erick Barrera
Correo: alamedagta21@mgail.com




