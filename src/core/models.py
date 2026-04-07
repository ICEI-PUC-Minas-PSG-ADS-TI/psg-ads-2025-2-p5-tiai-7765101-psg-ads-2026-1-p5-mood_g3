from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .managers import MoodEntryQuerySet

class MoodEntry(models.Model):
    class Emotion(models.TextChoices):
        MUITO_FELIZ = "MUITO_FELIZ", "Muito Feliz"
        FELIZ = "FELIZ", "Feliz"
        NEUTRO = "NEUTRO", "Neutro"
        TRISTE = "TRISTE", "Triste"
        MUITO_TRISTE = "MUITO_TRISTE", "Muito Triste"
        CANSADO = "CANSADO", "Cansado"
        ANSIOSO = "ANSIOSO", "Ansioso"
        ALIVIADO = "ALIVIADO", "Aliviado"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mood_entries")
    created_at = models.DateTimeField(auto_now_add=True)
    
    intensity_level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Escala de 1 a 5"
    )
    
    emotion = models.CharField(
        max_length=20,
        choices=Emotion.choices,
        default=Emotion.NEUTRO
    )
    
    notes = models.TextField(blank=True, null=True)

    objects = MoodEntryQuerySet.as_manager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mood Entry"
        verbose_name_plural = "Mood Entries"

    def __str__(self) -> str:
        return (
            f"{self.user.username} - {self.get_emotion_display()} "
            f"({self.intensity_level}/5) on "
            f"{self.created_at:%Y-%m-%d}"
        )