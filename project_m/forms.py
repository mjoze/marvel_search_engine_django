
from django.forms import ModelForm, TextInput
from .models import Hero


class HeroForm(ModelForm):
    class Meta:
        model = Hero
        fields = ['name']
        widgets = {'name': TextInput(
            attrs={'class': 'input', 'placeholder': 'Hero Name'})}
