from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
@receiver(post_save, sender=User)
def create_customer(sender,created,instance,*args, **kwargs):
    if created:
        customer = Client.objects.create(user=instance)
        Vehicle.objects.create(owner=customer)

@receiver(post_save, sender=User)
def save(sender,instance,**kwargs):
    instance.client.save()
    