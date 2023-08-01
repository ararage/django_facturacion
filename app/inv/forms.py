from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'descripcion',
            'estado'
        ]
        labels = {
            'descripcion': 'Descripción de la Categoría',
            'estado': 'Estado'
        }
        widget = {
            'descripcion': forms.TextInput
        }
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
