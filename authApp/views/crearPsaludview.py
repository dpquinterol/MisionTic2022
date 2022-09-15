from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from authApp.Serializers.Psaludserializer import PersonalSaludSerializer

class CrearPersonalSaludView(views.APIView):
    def post(self, request, **kwargs):
        serializar=PersonalSaludSerializer(data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_201_CREATED)
        return Response(serializar.errors,status=status.HTTP_400_BAD_REQUEST)