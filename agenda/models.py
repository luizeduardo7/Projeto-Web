from django.db import models
from usuarios.models import Usuario
from barbearia.models import *

class Agenda(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
   