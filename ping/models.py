from django.db import models

class Maquina(models.Model):
    nombre = models.CharField(max_length=5)
    #ip = models.IPAddressField()
    
    def __unicode__(self):
        return self.nombre
