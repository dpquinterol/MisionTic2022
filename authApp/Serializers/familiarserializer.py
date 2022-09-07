from dataclasses import fields
from  authApp.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model:Familiar
        fields='__all__'