from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Producto, Cliente


class productoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['codigo', 'nombre', 'valor', 'descripcion']
        labels ={
            'codigo': 'Codigo', 
            'nombre': 'Nombre', 
            'valor': 'Valor', 
            'descripcion': 'Descripcion',
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese codigo', 
                    'id': 'codigo'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'id': 'Valor',
                    'placeholder': 'Ingrese Valor', 
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'id': 'Descripcion',
                    'placeholder': 'Ingrese descripcion', 
                }
            ),
        }

class clienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['nombre','correo', 'rut', 'telefono', 'direccion']
        labels ={
            'nombre': 'Nombre',  
            'correo': 'Correo',
            'rut': 'Rut',
            'telefono': 'telefono',
            'direccion': 'direccion'
            
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombre'
                }
            ),  
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su correo', 
                    'id': 'correo'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su rut', 
                    'id': 'rut',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su telefono', 
                    'id': 'telefono',
                }  
            ),              
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su direccion', 
                    'id': 'direccion',
                } 
            ),     
        }