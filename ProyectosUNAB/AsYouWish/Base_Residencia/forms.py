from django import forms

# iterable
LUGARES = (
    ("1", "Residencia1"),
    ("2", "Residencia2"),
    ("3", "Residencia3"),
    ("4", "Residencia4"),
    ("5", "Residencia5"),
)


# se crea la clase de las residencias
class ResidenciasForm(forms.Form):
    residencias_field = forms.ChoiceField(choices = LUGARES)