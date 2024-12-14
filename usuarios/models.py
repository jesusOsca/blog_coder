from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='perfil_imagenes/', blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set', 
        blank=True
    )
