from django.db import models


class Sala(models.Model):
    capacidade = models.IntegerField()
    disponivel = models.BooleanField(default=True, verbose_name='disponível');
    nome = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    inicio = models.DateTimeField(verbose_name='início')
    fim = models.DateTimeField()
    instrutor = models.CharField(max_length=250)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
