from django import forms
from .models import Comprador, Vendedor, Producto

class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields=["id_comprador","nombre_comprador","apellido_comprador","fono_comprador","dir_comprador","comuna_comprador","email_comprador","usuario_comprador","pass_comprador"]

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields=["id_vendedor","nombre_vendedor","apellido_vendedor","fono_vendedor","dir_vendedor","com_vendedor","email_vendedor","usuario_vendedor","pass_vendedor"]


class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields=["nombre_producto","unidad_medida","precio_producto","categoria","descripcion_producto","imagen","vendedor"]    