from django import forms
from .models import Divisa

class DivisaForm(forms.ModelForm):
    class Meta:
        model = Divisa
        fields = ['nombre', 'compra', 'venta', 'bandera']
