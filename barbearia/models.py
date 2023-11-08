from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=9)
    senha = models.CharField(max_length=10)

class Barbeiro(models.Model):
    nome = models.CharField(max_length=30)

class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    preço = models.DecimalField(max_digits=5, decimal_places=2)

class Agenda(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
