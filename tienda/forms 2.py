from django import forms
from .models import Disco, Pedido

class DiscoForm(forms.Form):
    artista = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Artista',
            'class': 'form-control form-control-lg'
        })
    )
    titulo = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Título del disco',
            'class': 'form-control form-control-lg'
        })
    )
    genero = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Género',
            'class': 'form-control form-control-lg'
        })
    )
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'email', 'disco_solicitado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu email'}),
            'disco_solicitado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Disco solicitado'}),
        }
