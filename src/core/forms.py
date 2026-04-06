from django import forms
from django.contrib.auth.models import User

from .models import MoodEntry


class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("Já existe uma conta com este e-mail.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data


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
