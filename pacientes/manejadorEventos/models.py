from django.db import models
from informacionPacienteinformacionPaciente.models import Paciente

class Evento(models.Model):
    TIPO_EVENTO = [('Consulta médica','Consulta médica'),
                      ('Cirugia','Cirugia'),
                      ('Prescripción médicamento','Prescripción médicamento'),
                      ('EEG','EEG'),
                      ('MRI','MRI'),
                      ('miRNA','miRNA')]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPO_EVENTO)
    doctorEncargado = models.CharField(max_length=50)
    resultado = models.CharField(max_length=500, null = True,blank=True)
    fecha = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=500, null=True,blank=True)



