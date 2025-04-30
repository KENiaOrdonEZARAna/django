from django import forms
from .models import Cliente

# Definimos el formulario para el modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Especificamos el modelo del formulario
        fields = ['nombre', 'email', 'telefono', 'direccion']  # Especificamos los campos que queremos en el formulario
