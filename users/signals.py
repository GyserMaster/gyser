from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # sender - model User
    # instance - concrete user created in this moment "Jhonny93"
    # created - True
    print(f'create_profile: created - {created}')
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print(f'save_profile: instance - {instance}')
    instance.profile.save()