from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from apptienda.models import Cliente
from .serializers import ClientesSerializer

@csrf_exempt
@api_view (['GET', 'POST'])
def lista_clientes(request):
    if request.method=='GET':
        cliente = Cliente.objects.all()
        serializer = ClientesSerializer(cliente, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
