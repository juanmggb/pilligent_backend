from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save, post_save, post_delete
import os
from django.core.files.storage import default_storage
from django.core.files import File
from django.contrib.auth.models import User
from django.core.cache import cache

from .models import Usuario

#@receiver(pre_delete, sender=Usuario)
#def delete_usuario_image(sender, instance, **kwargs):
    # Eliminar la imagen del usuario si existe
#    if instance.profile_picture:
#        if os.path.isfile(instance.profile_picture.path):
#            os.remove(instance.profile_picture.path)

#@receiver(pre_save, sender=Usuario)
#def delete_previous_usuario_image(sender, instance, **kwargs):
    # Obtener el objeto Usuario antes de la actualización
#    if instance.pk:
#        previous_usuario = Usuario.objects.get(pk=instance.pk)
#        # Eliminar la imagen del usuario si existe
#        if previous_usuario.profile_picture and previous_usuario.profile_picture != instance.profile_picture:
#            if os.path.isfile(previous_usuario.profile_picture.path):
#                os.remove(previous_usuario.profile_picture.path)

#@receiver(pre_save, sender=Usuario)
#def set_default_usuario_image(sender, instance, **kwargs):
    # Asignar la imagen por default al usuario si no se le asignó una
#    if not instance.profile_picture:
#        default_image_path = "imagenes/default/usuario_default.png"
#        default_image = default_storage.open(default_image_path)
#        instance.profile_picture.save("usuario_default.png", File(default_image), save=False)

@receiver(post_save, sender=User)
def create_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_usuario(sender, instance, **kwargs):
    try:
        instance.usuario.save()
    except:
        Usuario.objects.create(user=instance)
