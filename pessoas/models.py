from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=300)
    data_vencimento = models.DateField(blank=True, null=True)
    valor_contrato = models.FloatField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
