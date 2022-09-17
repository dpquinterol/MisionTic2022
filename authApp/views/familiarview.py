from ast import Delete
from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.familiar import Familiar
from authApp.Serializers.familiarserializer import FamiliarSerializer

class CrearFamiliarView(views.APIView):
    def post(self, request):
        serializar=FamiliarSerializer(data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_201_CREATED)
        return Response(serializar.errors,status=status.HTTP_400_BAD_REQUEST)

class FamiliarView(views.APIView):

    def get(self, request, pk, format=None):
        model=Familiar.objects.get(pk=pk)
        serializer=FamiliarSerializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model=Familiar.objects.get(pk=pk)
        serializer=FamiliarSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        modelo=Familiar.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)