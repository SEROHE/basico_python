from django.db import models
from django.utils import timezone


# Creación de campos de la tabla ''
class AgendaPersonal(models.Model):
    nombre = models.CharField(max_length=45, default='DEFAULT VALUE')
    apellidos = models.CharField(max_length=45, default='DEFAULT VALUE')
    telefono = models.CharField(max_length=15, default='DEFAULT VALUE')

    class Meta:
        db_table = 'agenda_personal'