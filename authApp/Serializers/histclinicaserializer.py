from authApp.models.hist_clinica import Historia_clinica
from rest_framework import serializers

class HistoriaClinicaSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Historia_clinica
        fields='__all__'