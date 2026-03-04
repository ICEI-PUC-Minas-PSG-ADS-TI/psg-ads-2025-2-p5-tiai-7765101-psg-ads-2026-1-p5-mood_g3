from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MoodEntry


@receiver(post_save, sender=MoodEntry)
def on_mood_entry_created(sender, instance, created, **kwargs):
    if created:
        pass
