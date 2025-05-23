from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado para CryptoMinePro Web.
    Extiende AbstractUser para incluir campos de rol (Estudiante, Administrador).
    """
    # Campos booleanos para los roles específicos
    is_student = models.BooleanField(default=False, help_text='Designa si el usuario tiene rol de estudiante.')
    is_admin_user = models.BooleanField(default=False, help_text='Designa si el usuario tiene rol de administrador de la plataforma.')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'