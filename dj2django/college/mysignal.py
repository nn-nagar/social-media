from django.contrib.auth.models import User
from django.db.models.signals import post_save
from college.models import Profile
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwa):
    if created:
        Profile.objects.create(user=instance)
