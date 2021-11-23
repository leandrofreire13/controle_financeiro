from django import forms

from django.forms import TextInput

from .models import Gasto, Categoria


class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = [
            'categoria',
            'descricao',
            'valor',
            'vencimento',
            'status'
        ]
        widgets = {
            'descricao': TextInput(attrs={
                'class': "form-control"
            }),
            'valor': TextInput(attrs={
                'class': "form-control"
            }),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome'
        ]