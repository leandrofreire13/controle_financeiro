import datetime

from django.db import models

# Create your models here.


STATUS = (
    ('Comprado', 'COMPRADO'),
    ('Lançado na fatura', 'LANCADO_NA_FATURA'),
    ('Pago', 'PAGO')
)

class Categoria(models.Model):
    nome = models.CharField(max_length=200)


class Gasto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    vencimento = models.DateField(default=datetime.time)
    status = models.CharField(choices=STATUS, max_length=200, default='Comprado')