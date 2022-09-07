from django.db import models
from .usuario import Usuario

class Personal_salud(models.Model):
    id_Psalud=models.AutoField(primary_key=True)
    username=models.ForeignKey(Usuario,related_name='Psalud',on_delete=models.CASCADE)
    rol=models.CharField('Rol',max_length=35)
    espacialidad=models.CharField('Especialidad', max_length=35)