from urllib import request, response
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.Serializers.usuarioserializer import UsuarioSerializer

class CrearUsuarioView(views.APIView):
    def post(self, request, **kwargs):
        serializer=UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData={
            "username":request.data["username"],
            "password":request.data["password"],
        }

        tokenSerializer= TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validate_data, status=status.HTTP_201_CREATED)

from authApp.models.usuario import Usuario
class UsuarioView(views.APIView):
    def get(self, request, pk, format=None):
        model=Usuario.objects.get(pk=pk)
        serializer=UsuarioSerializer(model)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        model=Usuario.objects.get(pk=pk)
        serializer=UsuarioSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        modelo=Usuario.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
