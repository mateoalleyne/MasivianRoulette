from django import forms
from .models import *

class playerForm(forms.ModelForm):
    class Meta:
        model=Player
        fields='__all__'

class rouletteForm(forms.ModelForm):
    class Meta:
        model=Roulette
        fields='__all__'

class betForm(forms.ModelForm):
    class Meta:
        model=Bet
        fields='__all__'