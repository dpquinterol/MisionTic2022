from django.db import models
from .paciente import Paciente

class Signos_vitales(models.Model):
    id_sigvitales=models.AutoField(primary_key=True)
    id_paciente=models.ForeignKey(Paciente, related_name='sig_vitales', on_delete=models.CASCADE)
    oximetria=models.IntegerField(default=0)
    frecuencia_card=models.IntegerField(default=0)
    frecuencia_resp=models.IntegerField(default=0)
    temperatura=models.IntegerField(default=0)
    glicemias=models.IntegerField(default=0)
    presion_art=models.IntegerField(default=0)
    fecha_registro=models.DateTimeField()