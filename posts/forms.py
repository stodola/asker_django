from django.contrib.auth.models import User
from django import forms
from .models import Pytania


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"User name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']


class PytaniaForm(forms.ModelForm):
    pytanie= forms.TextInput(attrs={'class': 'form-control','placeholder':"User name"})
    user = forms.TextInput(attrs={'class': 'form-control','placeholder':"User name"})
    class Meta:
        model = Pytania
        widgets = {
                         #   'user': forms.TextInput(attrs={'class': 'form-control'}),
                            'pytanie': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
                            'odpowiedz': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
                            'carddeck': forms.TextInput(attrs={'class': 'form-control'}),
                                    }

        fields = ['pytanie', 'odpowiedz','carddeck']



