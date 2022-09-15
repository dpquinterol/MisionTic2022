from authApp.models.sig_vitales import Signos_vitales
from rest_framework import serializers

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Signos_vitales
        fields=('id_paciente','oximetria','frecuencia_card','frecuencia_resp','temperatura','glicemias','presion_art','fecha_registro')