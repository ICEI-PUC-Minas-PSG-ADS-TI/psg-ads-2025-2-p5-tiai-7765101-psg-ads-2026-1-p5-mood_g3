from django import forms

from .models import MoodEntry


class MoodEntryForm(forms.ModelForm):

    class Meta:
        model = MoodEntry
        fields = ["emotion", "intensity_level", "notes"]
        widgets = {
            "emotion": forms.Select(
                attrs={"class": "form-select"},
            ),
            "intensity_level": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "max": 10,
                    "placeholder": "1 – 10",
                },
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "How are you feeling? (optional)",
                },
            ),
        }
