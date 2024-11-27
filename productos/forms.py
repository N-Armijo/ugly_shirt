from django import forms
from .models import Polera

class PoleraForm(forms.ModelForm):
    class Meta:
        model = Polera
        fields = ['nombre', 'descripcion', 'precio']

        #widgets permite personalizar con la apariencia del formulario para que no sea tan feo
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la polera'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la polera'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio de la polera'}),
        }
