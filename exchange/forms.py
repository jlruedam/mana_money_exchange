from django import forms
from .models import Divisa

class DivisaForm(forms.ModelForm):
    class Meta:
        model = Divisa
        fields = ['nombre', 'compra', 'venta', 'bandera']

    def __init__(self, *args, flag_choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        if flag_choices is not None:
            self.fields['bandera'] = forms.ChoiceField(
                choices=flag_choices,
                widget=forms.Select(attrs={'class': 'form-control'})
            )

        # Apply 'form-control' class to other fields as well
        for field_name, field in self.fields.items():
            if field_name != 'bandera': # 'bandera' already has the class
                field.widget.attrs['class'] = 'form-control'
