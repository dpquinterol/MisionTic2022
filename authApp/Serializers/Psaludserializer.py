from authApp.models.Psalud import Personal_salud
from rest_framework import serializers

class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personal_salud
        fields=('username','rol','especialidad')