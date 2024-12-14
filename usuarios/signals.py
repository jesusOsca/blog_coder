from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Bienvenido a nuestro blog'
        message = f'Hola {instance.username}, bienvenido a nuestro blog.'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])
