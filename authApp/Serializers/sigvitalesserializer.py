from dataclasses import fields
from authApp.models.sig_vitales import Signos_vitales
from rest_framework import serializers

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Signos_vitales
        fields='__all__'