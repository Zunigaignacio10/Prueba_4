from rest_framework import serializers
from apptienda.models import Cliente


class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields=['rut','nombre', 'correo', 'telefono', 'direccion']