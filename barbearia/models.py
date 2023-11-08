from django.db import models
from usuarios.models import Usuario


class Barbeiro(models.Model):
    nome = models.CharField(max_length=30)

class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

