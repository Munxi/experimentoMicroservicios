from django.db import models

class Evento(models.Model):
    TIPO_EVENTO = [('Consulta médica','Consulta médica'),
                      ('Cirugia','Cirugia'),
                      ('Prescripción médicamento','Prescripción médicamento'),
                      ('EEG','EEG'),
                      ('MRI','MRI'),
                      ('miRNA','miRNA')]
    ni_paciente = models.IntegerField()
    tipo = models.CharField(max_length=50, choices=TIPO_EVENTO)
    doctor_id = models.IntegerField()
    resultado = models.CharField(max_length=500, null = True,blank=True)
    fecha = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=500, null=True,blank=True)



