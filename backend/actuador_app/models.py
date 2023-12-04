from django.db import models

class Actuador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique=True)
    estado = models.BooleanField(default=False)
    pin_gpio = models.IntegerField()
    #distancia_total = models.FloatField(default=0.0)
    #posicion_actual = models.FloatField(default=0.0)
    repeticiones = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nombre
