from django import forms
from .models import Divisa

class DivisaForm(forms.ModelForm):
    class Meta:
        model = Divisa
        fields = ['nombre', 'compra', 'venta', 'bandera']

    def __init__(self, *args, flag_choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # The choices for 'bandera' will be rendered manually in the template
        # We still need to ensure the widget is a Select and has the class
        self.fields['bandera'].widget = forms.Select(attrs={'class': 'form-control'})

        # Apply 'form-control' class to other fields
        for field_name, field in self.fields.items():
            if field_name != 'bandera': 
                field.widget.attrs['class'] = 'form-control'
