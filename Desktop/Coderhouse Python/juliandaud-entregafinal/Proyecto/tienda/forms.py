from django import forms
from .models import Pedido


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


class PedidoDiscoForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    disco_solicitado = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class PedidoEditarForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'email', 'disco_solicitado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'disco_solicitado': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DiscoBusquedaForm(forms.Form):
    artista = forms.CharField(
        required=False,
        label="Artista",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Artista'
        })
    )
    titulo = forms.CharField(
        required=False,
        label="Título",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Título'
        })
    )
    genero = forms.CharField(
        required=False,
        label="Género",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Género'
        })
    )
