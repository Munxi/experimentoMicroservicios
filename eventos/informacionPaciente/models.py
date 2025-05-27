from django.db import models

class Paciente(models.Model):
    SEXOS = [
        ('M', 'Masculino'),
        ('F', 'Femenino')]
    EPS = [('Nueva EPS','Nueva EPS'),
           ('Salud Total','Salud Total'),
           ('Famisanar','Famisanar'),
           ('Sanitas','Sanitas')]
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    NI = models.IntegerField(primary_key=True)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=15, choices=SEXOS)
    eps = models.CharField(max_length=30, choices=EPS)





