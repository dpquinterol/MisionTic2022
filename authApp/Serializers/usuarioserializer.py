from dataclasses import field
from authApp.models.usuario import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model: Usuario
        field ='__all__'