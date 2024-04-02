from django.db import models
from django.utils import timezone

# Create your models here.
class Votacion(models.Model):
    anio=models.IntegerField(default=0)
    partido= models.CharField(max_length=45)
    voto = models.IntegerField(default=0)

    class Meta:
        db_table = 'votacion'

    def calcular_porcentaje_votos(self, total_votos):
        if total_votos == 0:
            return 0
        else:
            return (self.voto / total_votos) * 100