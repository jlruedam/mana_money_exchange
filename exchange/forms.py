from django import forms
from .models import Divisa

class DivisaForm(forms.ModelForm):
    class Meta:
        model = Divisa
        fields = ['nombre', 'compra', 'venta', 'bandera']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
