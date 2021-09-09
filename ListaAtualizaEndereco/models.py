from django.conf import settings
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    NomeMae = models.CharField(max_length=200)
    datanascimento = models.DateField(blank=True, null=True)
    dataCadastro = models.DateField(default=timezone.now)

    def incluir(self):
        self.save()

    def __str__(self):
        return self.nome

    def alterar(self):
        self.save()

    def excluir(self):
        self.excluir()
