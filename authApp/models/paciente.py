from django.db import models
from .usuario import Usuario
from .Psalud import Personal_salud

class Paciente(models.Model):
    id_paciente=models.AutoField(primary_key=True)
    id_Psalud=models.ForeignKey(Personal_salud,related_name='paciente',on_delete=models.CASCADE)
    username=models.ForeignKey(Usuario,related_name='paciente', on_delete=models.CASCADE)
    direccion=models.CharField('Direccion', max_length=35)
    ciudad=models.CharField('Ciudad', max_length=35)
    fecha_nacimiento=models.DateField()
